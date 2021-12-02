from flask import Blueprint, render_template, request, flash, jsonify
from flask.helpers import url_for
from flask.templating import render_template_string
from werkzeug.utils import redirect
from project import views, views, auth
from .db_config import create_db

mysql = create_db()

add = Blueprint('add', __name__)

# # TODO: change the route endpoint abd I may need to remove the index function
@add.route('/', methods=['GET', 'POST'])
def index():
    print("hellooo")
    if request.method == 'POST':
        details = request.form
        course_id = details.get('course_id')
        course_name = details.get('course_name')
        dept_name = details.get('dept_name')
        cur = mysql.connection.cursor()
        print(course_id, course_name)
        print("searching...")
        cur.execute("SELECT CourseID,Title,DepartmentName,Credits,ModesOfInstruction FROM Course WHERE CourseID = %s OR   Title = %s OR DepartmentName= %s" , [course_id, course_name, dept_name])
        result = cur.fetchall()
        print(type(result)) 
        if result[0] != None:
            #return render_template('output.html', headings = ("CourseID","Title","DepartmentName","Credits","ModesOfInstruction") ,variable = result)
            return redirect(url_for('output', data = result))

    return render_template('search_course.html')

@add.route('/add/<data>', methods=['GET', 'POST'])
def output(data):
    data = list(eval(data))   
    if request.method == "GET":

        option = request.form.get("ADD")
        print("hello")
        # if option == "ADD1":
        cursor = mysql.connection.cursor()
        a = "23100278"
        b = "CS100"
        c= "S2"
        d = "B+"
        cursor.execute("INSERT INTO Takes(StudentID, CourseID, SectionID, Grade) VALUES(%s,%s ,%s , %s)", (a,b,c,d))
        mysql.connection.commit()
        cursor.close()  
    return render_template('output.html', headings = ("CourseID","Title","DepartmentName","Credits","ModesOfInstruction") , variable = data)
