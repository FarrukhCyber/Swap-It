from flask import Blueprint, render_template, request, flash, jsonify
from flask.helpers import url_for
from flask.templating import render_template_string
from werkzeug.utils import redirect
from project import views, views, auth
from .db_config import create_db
from project.auth import session, login_required

mysql = create_db()

add = Blueprint('add', __name__)

# TODO: Handle the case if the user tries to add an already added course
@add.route('/add', methods=['GET', 'POST'])
@login_required
def index():
    if request.method == 'POST':
        details = request.form
        course_id = details.get('course_id')
        user_id = session["user"][0]
        
        cur = mysql.connection.cursor()
        cur.execute("SELECT CourseID, SectionID from section WHERE CourseID = %s" , [course_id])
        result = cur.fetchall()
        cur.close()
        
        print("Result:", result)
        if result[0] != None:
            session["add"] = result
            return redirect(url_for('add.output'))
        
    return render_template('add.html', session=session)

@add.route('/add2', methods=['GET', 'POST'])
@login_required
def output():
    if request.method == "POST":
        details = request.form.get("options")
        details_list = details.split('/')
        course_id = details_list[0] #gives me the course ID
        sec_id = details_list[1]    #gives me the Section ID
        user = session["user"][0]
        grade = "None"

        to_pass = [user,course_id,sec_id,grade]
        session["add_details"] = to_pass
        return redirect(url_for("add.insert_data"))

    data = []
    rows = session["add"]
    
    data = [ row for row in rows]
    print("Data:", data)
    return render_template('add_output.html' , data = data, status = session["status"])


@add.route('/add3', methods=['GET', 'POST'])
@login_required
def insert_data():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM takes WHERE StudentID=%s AND CourseID=%s AND SectionID=%s",session["add_details"][0:3])
    result = cursor.fetchall()
    
    if len(result) == 0 :
        cursor.execute("INSERT INTO takes(StudentID, CourseID, SectionID, Grade) VALUES(%s,%s ,%s , %s)", session["add_details"])
        mysql.connection.commit()
        session["status"] = True
    else:
        session["status"] = False
        
    cursor.close()
    return redirect(url_for("add.output"))
    