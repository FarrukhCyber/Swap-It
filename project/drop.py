from flask import Blueprint, render_template, request, flash, jsonify
from flask.helpers import url_for
from werkzeug.utils import redirect
from project.auth import session, login_required
from .db_config import create_db
from project import views

mysql = create_db()

drop = Blueprint('drop', __name__)

#Testing---------------
# global_list = [
#     ('PHY101', 'Modern Physics', 4),
#     ('PHY200', 'Advance Physics', 3),
#     ('CAL101', ' Calculus-I', 4),
#     ('CAL102', ' Calculus-II', 4),
    
# ]
#-----------------------

@drop.route('/drop', methods=['GET', 'POST'])
@login_required
def fetch_data():
    user_id = session["user"][0]
    print("USer:", user_id)
    cur = mysql.connection.cursor()
    value = cur.execute("SELECT CourseID, SectionID FROM takes WHERE StudentID=%s", [user_id])
    # if the student has enrolled courses
    if value >0:
        result = cur.fetchall()
        course_id = [ row[0] for row in result ] # gets the course ID
        course_title = []
        course_credits = []
        for id in course_id:
            cur.execute("SELECT Title, Credits FROM course WHERE CourseID=%s", [id])
            r = cur.fetchall()
            course_title.append(r[0][0])   #get corrosponding title
            course_credits.append(r[0][1]) #get the corrosponding credit hours
        
        cur.close()
        final_result = [ (course_id[i], course_title[i], course_credits[i]) for i in range(len(course_id))]
        print(final_result)
        session["drop"] = final_result
    
    else:
        session["drop"] = -1 # No more enrolled courses
    
    # #TESTING------------
    # if len(global_list) != 0 :
    #     session["drop"] = global_list
    # else:
    #     session["drop"] = -1
    # #---------------------------
    return redirect(url_for("drop.show_data"))
    
    
@drop.route('/drop2', methods=['GET', 'POST'])
@login_required
def show_data():
    if request.method == "POST" :
        course_id = request.form.get('options')
        user_id = session["user"][0] 
        print("Course_id:", course_id)
        
        # delete that course from the table
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM takes WHERE StudentID=%s AND CourseID=%s", [user_id, course_id])
        mysql.connection.commit()
        cur.close()
        
        # #TESTING------------
        # remove = ()
        # for row in global_list:
        #     if course_id in row:
        #         remove = row
        #         break
                
        # global_list.remove(remove)
        # #------------------------
        return redirect(url_for("drop.fetch_data"))
        
    # result is a list of tuples where each tuple has id, title and crd hrs
    result = session["drop"] 
    flag = True
    if result == -1:
        flag = False
        
    return render_template("drop.html", data= result, flag=flag)
    

















# @drop.route('/drop', methods=['GET', 'POST'])
# def drop_course():
#     if request.method == "POST":
#         print("inside POST IF")
#         user_id = request.form.get("options")
#         return f"<h1>user_id<h1>"

#     else:
#         user_id = session["user"][0]
#         print("USer:", user_id)
#         cur = mysql.connection.cursor()
#         value = cur.execute("SELECT CourseID, SectionID FROM takes WHERE StudentID=%s", [user_id])
#         result = cur.fetchall()
#         # print(result)
#         # return redirect(url_for('views.home_page'))
#         print("I'm going to return")
#         return render_template("drop.html", data= result)
#         # cur.close()
#         # try:
#         #     try:
#         #         cur.execute("SELECT CourseID, SectionID FROM takes WHERE StudentID=%s", [user_id])
#         #     # NB : you won't get an IntegrityError when reading
#         #     except (MySQLdb.Error, MySQLdb.Warning) as e:
#         #         print(e)
#         #         return e
#         #     try:
#         #         result = cur.fetchall()
#         #         return result
#         #     except TypeError as e:
#         #         print(e)
#         #         return e

#         # finally:
#         #     cur.close()
            
