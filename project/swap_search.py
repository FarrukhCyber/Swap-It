from flask import Blueprint, render_template, request, flash, jsonify
from flask.helpers import url_for
from flask.templating import render_template_string
from werkzeug.utils import redirect
from project import views, views, auth
from .db_config import create_db
from project.auth import session, login_required

mysql = create_db()

swap_search = Blueprint('swap_search', __name__)

@swap_search.route("/swap_search", methods=['GET', 'POST'])
@login_required
def search():
    data = []
    flag = False
    
    if request.method == "POST":
        # Just do the search:
        if "find" in request.form:
            haveID = request.form.get("have")
            wantID = request.form.get("want")
            userID = session["user"][0]
            data = fetch_data(haveID, wantID)
            flag = data != -1
        else:
            details = request.form.get("options")
            details = details.split("/")
            send_accept(details)
    
    return render_template("swap_search.html", data=data, flag=flag)


#utility functions
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
    
def fetch_data(haveID, wantID):
    #Filter: Have only
    if len(wantID)==0:
        query = "SELECT RequestID, HaveCourseID, WantCourseID FROM swapit WHERE HaveCourseID=%s AND Status=%s"
        args = [haveID, "0"]
    
    #Filter: Want Only
    elif len(haveID)==0:
        query = "SELECT RequestID, HaveCourseID, WantCourseID FROM swapit WHERE WantCourseID=%s AND Status=%s"
        args = [wantID, "0"]
        
    #Filter: With Both haveID and wantID
    else:
        query = "SELECT RequestID, HaveCourseID, WantCourseID FROM swapit WHERE HaveCourseID=%s AND WantCourseID=%s AND Status=%s"
        args = [haveID, wantID, "0"]
          
    result = handle_query(query, args, False)
    
    #Check if there are any pending Swap Requests
    if len(result) >0:
        return result
    else:
        return -1 # shows that there are no more swap requests

def send_accept(data):
    query = "UPDATE swapit SET AcceptID=%s, Status=%s WHERE  RequestID=%s AND HaveCourseID=%s AND WantCourseID=%s"
    user = session["user"][0]
    args = [user, "1", data[0], data[1], data[2]]
    _ = handle_query(query, args, True)