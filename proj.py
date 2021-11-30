from flask import Flask,render_template, request
from werkzeug.utils import redirect
from flask_mysqldb import MySQL
from flask.templating import render_template_string
from flask.helpers import url_for

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'flaskapp'
mysql = MySQL(app)
 
@app.route('/', methods=['GET', 'POST'])

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

@app.route('/add/<data>', methods=['GET', 'POST'])
def output(data):
    if request.method == "POST":
        print("farrukh")
        option = request.form.get("ADD")
        if option == "ADD1":
            cursor = mysql.connection.cursor()
            cursor.execute("INSERT INTO Takes(StudentID, CourseID, SectionID, Semester, Year_, Grade) VALUES(user_id, name, password, email,12,dept)")
            mysql.connection.commit()
            cursor.close() 
        
    return render_template('output.html', headings = ("CourseID","Title","DepartmentName","Credits","ModesOfInstruction") , variable = data)


@app.route('/swap', methods=['GET', 'POST'])
def swap_search():
    return render_template('swap_search.html')

if __name__ == "__main__":
    app.run(debug=True)