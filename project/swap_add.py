from flask import Blueprint, render_template, request, flash, jsonify
from flask.helpers import url_for
from flask.templating import render_template_string
from werkzeug.utils import redirect
from project import views, views, auth
from .db_config import create_db
from project.auth import session

mysql = create_db()

swap_add = Blueprint('swap_add', __name__)

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

def validate(userID, haveID):
    query = "SELECT StudentID, CourseID FROM takes WHERE StudentID=%s AND CourseID=%s "
    args = [userID, haveID]
    data = handle_query(query, args, False)
    if len(data) > 0:
        return True
    else:
        return False
    
    
@swap_add.route("/swap_add", methods=['GET', 'POST'])
def add_rquest():
    flag = True
    if request.method == "POST":
        haveID = request.form.get("have")
        wantID = request.form.get("want")
        userID = session["user"][0]
        # userID = "23100243"  # For TESTING Purpose, REMOVE for actual running----------
        
        query = "INSERT INTO swapit VALUES(%s,%s,%s,%s,%s)"
        args = [userID, haveID, wantID, "-1", "0"]
        
        #Validation that user must be enrolled in HAVE Course
        flag = validate(userID, haveID)
        
        if flag:
            handle_query(query, args, True)
            flash("Swap Request added successfully")
        else:
            flash("Swap Request Failed becuase you are not enrolled in HaveCourse")
            
    return render_template("swap_add.html", flag=flag)