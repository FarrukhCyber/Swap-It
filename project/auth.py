from flask import Blueprint, render_template, request, flash, jsonify
from flask.helpers import url_for
from flask.templating import render_template_string
from werkzeug.utils import redirect
from flask import session
import functools

# random comment 

from project import views
from project import admin
from .db_config import create_db
# from flask_login import login_user, login_required, logout_user, current_user

mysql = create_db()

auth = Blueprint('auth', __name__)


#this decorator func implements the login required functionality
def login_required(func):
    @functools.wraps(func)
    def secure_function(*args, **kwargs):
        if "user" not in session:
        #     return redirect(url_for("login"))
        # return func
            return redirect(url_for("auth.login", next=request.url))
        return func(*args, **kwargs)

    return secure_function


# @auth.route('/', methods=['GET', 'POST'])
@auth.route('/swap-it123.herokuapp.com/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        details = request.form
        user_id = details.get('user_id')
        password = details.get('password')
        option = details.get('options')
        print(user_id, password)
        cur = mysql.connect.cursor()
        if option == 'admin':
            print("IN ADMIN")
            resultValue = cur.execute("SELECT AdminID,AdminPassword FROM Admin WHERE AdminID = %s and AdminPassword = %s", [user_id, password])
            if resultValue > 0 :
                result = cur.fetchall()
                print("Result:", result)
                value = (user_id, option)
                session["user"] = value
                print(session["user"])
                cur.close()
                return redirect(url_for('admin.admin_page'))

            else:
                # flash('Wrong Credentials', category='error')
                print("wrong credentials")
                cur.close()
                return redirect(url_for('auth.login'))
                # add flash
        else:
            print("IN STUDENT")
            resultValue = cur.execute("SELECT StudentID,Password_ FROM Student WHERE StudentID = %s and Password_ = %s", [user_id, password])
            if resultValue > 0 :
                result = cur.fetchall()
                print("Result:", result)
                value = (user_id, option)
                session["user"] = value
                print(session["user"])
                cur.close()
                return redirect(url_for('views.home_page'))

            else:
                # flash('Wrong Credentials', category='error')
                print("wrong credentials")
                cur.close()
                return redirect(url_for('auth.login'))
                # add flash

        # mysql.connection.commit()
    return render_template("login2.html")

#Original Function
# @auth.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         details = request.form
#         email = details.get('email')
#         password = details.get('password')
#         option = details.get('options')
#         print(email, password)
#         cur = mysql.connect.cursor()
#         if option == 'admin':
#             print("IN ADMIN")
#             cur.execute("SELECT AdminEmail,AdminPassword FROM Admin WHERE AdminEmail = %s and AdminPassword = %s", [email, password])
#             result = cur.fetchall()
#             cur.execute("SELECT * FROM Admin WHERE AdminEmail = %s and AdminPassword = %s", [email, password])
#             user = cur.fetchall()
#             # user = user[0]
#             print(result)
#             if result:
#                 result = result[0]
#                 print(result)
#                 # login_user(user, remember=True)
#                 # Adding session details, which will store tuple (id, admin/student) against a key
#                 value = (email, option)
#                 session["user"] = value
#                 print(session["user"])
#                 return redirect(url_for('views.home_page'))
#             else:
#                 # flash('Wrong Credentials', category='error')
#                 print("wrong credentials")
#                 return redirect(url_for('auth.login'))
#                 # add flash
#         else:
#             print("IN STUDENT")
            
#             cur.execute("SELECT Email,Password_ FROM Student WHERE Email = %s and Password_ = %s", [email, password])
#             result = cur.fetchall()
#             cur.execute("SELECT * FROM Student WHERE Email = %s and Password_ = %s", [email, password])
#             user = cur.fetchall()
#             # user = user[0]
#             # result = result[0]
#             print(result)
#             cur.close()
#             if result:
#                 result = result[0]
#                 print(result)
#                 # login_user(user, remember=True)
#                 return redirect(url_for('views.home_page'))
#                 # if email == result[0]:
#                 #     print("email right")
#                 #     if password == result[1]:
#                 #         print("password right")
#                 #         return "Logged in Successfully"
#                 #     else:
#                 #         print("new pass")
#                 #         return "Wrong Password"
#                 # else:
#                 #     return "Wrong Password or Email"
#             else:
#                 # flash('Wrong Credentials', category='error')
#                 print("wrong credentials") # add flash 
#                 return redirect(url_for('auth.login'))
#                 # return redirect(url_for('login2.html'))


#         # mysql.connection.commit()
#     return render_template("login2.html")


@auth.route('/logout')
# @login_required
def logout():
    # logout_user()
    # Reomivg the session details
    # session.pop("user", None)
    session.clear()
    return redirect(url_for('auth.login'))

@auth.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        user_id = request.form.get('user_id')   # Confirm with FrontEnd 
        email = request.form.get('email')       # Confirm with FrontEnd
        name = request.form.get('name')         # Confirm with FrontEnd
        password = request.form.get('password') # Confirm with FrontEnd
        option = request.form.get('options')    # Confirm with FrontEnd
        
        # VALIDATION CHECK---------------------------
        #Creating a connection cursor
        cursor = mysql.connect.cursor()
        
        #signup as an admin
        if option == "admin":
            result = cursor.execute("SELECT * FROM Admin WHERE AdminName=%s AND AdminEmail=%s", (name,email))
            
        #sign up as Student
        elif option == "student":
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
            #insert into student table
            if option == "student":
                cursor = mysql.connect.cursor()
                crd = "23"
                dept = "CS"
                cursor.execute("INSERT INTO student(StudentID ,StudentName, Password_, Email, TotalCreditHours,  DepartmentName) VALUES(%s,%s,%s,%s,%s,%s)", (user_id, name, password, email,crd,dept))
                cursor.connection.commit()
                # cursor.execute("SELECT * from stduent WHERE StudentID=%s", user_id)
                # user = cursor.fetchall()
                cursor.close() 
                # login_user(user, remember=True)
                # flash('Account created!', category='success')
                session["user"] = (user_id, option)
                print(session["user"])
                return redirect(url_for('views.home_page'))
            
            #insert into admin table
            elif option == "admin":
                cur = mysql.connect.cursor()
                cur.execute("INSERT INTO Admin VALUES (%s,%s,%s,%s)", (user_id, name, password, email))
                cursor.connection.commit()
                # cur.execute("SELECT * from Admin WHERE AdminID=%s", user_id)
                # user = cur.fetchall()
                cur.close() 
                # login_user(user, remember=True)
                # flash('Account created!', category='success')
                session["user"] = (user_id, option)
                print(session["user"])
                return redirect(url_for('views.home_page'))
    
    return render_template("sign_up.html")
