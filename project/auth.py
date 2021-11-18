from flask import Blueprint, render_template, request, flash, jsonify
from flask.helpers import url_for
from flask.templating import render_template_string
from werkzeug.utils import redirect
from .db_config import create_db
from flask_login import login_user, login_required, logout_user, current_user

mysql = create_db()

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        details = request.form
        email = details.get('email')
        password = details.get('password')
        option = details.get('options')
        print(email, password)
        cur = mysql.connection.cursor()
        if option == 'admin':
            print("IN ADMIN")
            cur.execute("SELECT AdminEmail,AdminPassword FROM Admin WHERE AdminEmail = %s and AdminPassword = %s", [email, password])
            result = cur.fetchall()
            cur.execute("SELECT * FROM Admin WHERE AdminEmail = %s and AdminPassword = %s", [email, password])
            user = cur.fetchall()
            # user = user[0]
            print(result)
            if result:
                result = result[0]
                print(result)
                # login_user(user, remember=True)
                return redirect(url_for('views.home_page'))
            else:
                # flash('Wrong Credentials', category='error')
                print("wrong credentials")
                return redirect(url_for('auth.login'))
                # add flash
        else:
            print("IN STUDENT")
            
            cur.execute("SELECT Email,Password_ FROM Student WHERE Email = %s and Password_ = %s", [email, password])
            result = cur.fetchall()
            cur.execute("SELECT * FROM Student WHERE Email = %s and Password_ = %s", [email, password])
            user = cur.fetchall()
            # user = user[0]
            # result = result[0]
            print(result)
            cur.close()
            if result:
                result = result[0]
                print(result)
                # login_user(user, remember=True)
                return redirect(url_for('views.home_page'))
                # if email == result[0]:
                #     print("email right")
                #     if password == result[1]:
                #         print("password right")
                #         return "Logged in Successfully"
                #     else:
                #         print("new pass")
                #         return "Wrong Password"
                # else:
                #     return "Wrong Password or Email"
            else:
                # flash('Wrong Credentials', category='error')
                print("wrong credentials") # add flash 
                return redirect(url_for('auth.login'))
                # return redirect(url_for('login2.html'))


        # mysql.connection.commit()
    return render_template("login2.html")


@auth.route('/logout')
def logout():
    return "LOGOUT"

@auth.route('/signup', methods=['GET', 'POST'])
def sign_up():
    return "SIGN UP"