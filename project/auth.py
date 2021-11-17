from flask import Blueprint, render_template, request, flash, jsonify
from flask.helpers import url_for
from werkzeug.utils import redirect

from project import views
from .db_config import create_db

mysql = create_db()

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return "LOGIN"


@auth.route('/logout')
def logout():
    return redirect(url_for('auth.login'))

@auth.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        user_id = request.form.get('user_id') # Confirm with FrontEnd 
        email = request.form.get('email')       # Confirm with FrontEnd
        name = request.form.get('firstName')    # Confirm with FrontEnd
        password = request.form.get('password') # Confirm with FrontEnd
        
        # VALIDATION CHECK---------------------------
        #Creating a connection cursor
        cursor = mysql.connection.cursor()
        
        #Executing SQL Statements, we will get number of entries in result
        result = cursor.execute("SELECT * FROM student WHERE StudentName=%s AND Email=%s", (name,email))
        cursor.close()
        
        if result>0:
            # flash('Email already exists.', category='error')
            print("User already exists")
            
        elif len(email) <4:
            # flash('Email must be greater than 3 characters.', category='error')
            print("Email must be greater than 3 characters.")
            
        elif len(name) <2:
            # flash('First name must be greater than 1 character.', category='error')
            print("Name must have greater than 2 characters")
            
        elif len(password) < 2:
            # flash('Password must be at least 3 characters.', category='error')
            print("very weak password")
        else:
            cursor = mysql.connection.cursor()
            crd = "23"
            dept = "CS"
            cursor.execute("INSERT INTO student(StudentID ,StudentName, Password_, Email, TotalCreditHours,  DepartmentName) VALUES(%s,%s,%s,%s,%s,%s)", (user_id, name, password, email,crd,dept))
            mysql.connection.commit()
            cursor.close() 
            
            # flash('Account created!', category='success')
            print("Account created")
            return redirect(url_for('views.home_page'))
    
    return render_template("sign_up.html")
            
            