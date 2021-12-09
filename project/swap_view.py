from flask import Blueprint, render_template, request, flash, jsonify
from flask.helpers import url_for
from flask.templating import render_template_string
from werkzeug.utils import redirect
from project import views, views, auth
from .db_config import create_db
from project.auth import session

mysql = create_db()

swap_view = Blueprint('swap_view', __name__)

#Testing---------------
global_list = [
    ( "23100001", "ECO111", "LANG110", "23100240", "1"),
    ( "23100001", "CS100", "REL212", "23100240", "1")
]
#-----------------------

#utility function
def handle_query(query, args, commit):
    cur = mysql.connect.cursor()
    cur.execute(query, args)
    
    if commit:
        cur.connection.commit()
        cur.close()
        return ()    
    else:
        result = cur.fetchall()
        cur.close()
        return result 
    
@swap_view.route("/swap_view", methods=['GET', 'POST'])
def view():
    userID = session["user"][0]
    query = "SELECT * FROM swapit WHERE RequestID=%s"
    args = [userID]
    data = handle_query(query, args, False)

    # To handle the case if the user has not added any requests
    flag=True
    if len(data) == 0:
        flag = False
        
    return render_template("swap_view.html", data=data, flag=flag)