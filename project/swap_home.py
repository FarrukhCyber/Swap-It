from flask import Blueprint, render_template, request, flash, jsonify
from flask.helpers import url_for
from flask.templating import render_template_string
from werkzeug.utils import redirect
from project import views, views, auth
from .db_config import create_db
from project.auth import session, login_required

mysql = create_db()

swap_home = Blueprint('swap_home', __name__)

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

@swap_home.route('/swap_home', methods=['GET', 'POST'])
@login_required
def fetch_data():
    query = "SELECT RequestID, HaveCourseID, WantCourseID FROM swapit WHERE Status=%s"
    args = ["0"]
    result = handle_query(query, args, False)
    
    #Check if there are any pending Swap Requests
    if len(result) >0:
        session["swap_home"] = result
    else:
        session["swap_home"] = -1 # shows that there are no more swap requests
        
    return redirect(url_for("swap_home.show_data"))


@swap_home.route('/swap_home2', methods=['GET', 'POST'])
@login_required
def show_data():
    if request.method == "POST":
        details = request.form.get("options")
        details = details.split("/")
        print(details)
        session["swap_home3"] = details
        return redirect(url_for("swap_home.send_accept"))
    
    data = session["swap_home"]
    flag = True
    
    #Handling case for no swap requests found
    if data == -1 :
        flag = False
        
    return render_template("swap_home.html", data= data, flag= flag)

@swap_home.route('/swap_home3', methods=['GET', 'POST'])
@login_required
def send_accept():
    query = "UPDATE swapit SET AcceptID=%s, Status=%s WHERE  RequestID=%s AND HaveCourseID=%s AND WantCourseID=%s"
    data = session["swap_home3"]
    user = session["user"][0]
    args = [user, "1", data[0], data[1], data[2]]
    _ = handle_query(query, args, True)
    
    return redirect(url_for("swap_home.fetch_data"))
    
    
        