from flask import Blueprint, render_template, request, flash, jsonify
from flask.helpers import url_for
from flask.templating import render_template_string
from werkzeug.utils import redirect
from project import views, auth, add
from .db_config import create_db
from project.auth import session

mysql = create_db()

search = Blueprint('search', __name__)

# FIXME: if only course ID is used for the search, it throughs "int object is not callable error in html template"
@search.route('/search', methods=['GET', 'POST'])
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
        cur.close()
        print(type(result)) 
        if result[0] != None:
            #return render_template('output.html', headings = ("CourseID","Title","DepartmentName","Credits","ModesOfInstruction") ,variable = result)
            session["search"] = result
            return redirect(url_for('search.output', data = result))

    return render_template('search_course.html')

@search.route('/search_output/<data>', methods=['GET', 'POST'])
def output(data):
    data = list(eval(data)) 
    print("check:", data    )
    r = session["search"]
    print("Value of r:", r)   
    return render_template('search_output.html', headings = ("CourseID","Title","DepartmentName","Credits","ModesOfInstruction") , variable = r)
