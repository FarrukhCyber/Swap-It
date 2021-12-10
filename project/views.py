from flask import Blueprint, render_template, request, flash, jsonify
from .db_config import create_db
from flask_login import login_required, current_user
from project.auth import session, login_required


mysql = create_db()

views = Blueprint('views', __name__)


@views.route('/home', methods=['GET', 'POST'])
@login_required
def home_page():
    # get info from the backend
    # id = session["user"][0]
    # print("ID:", id, type(id))
    # cur = mysql.connection.cursor()
    # if "user" in session:
    #     id = session["user"][0]
    #     print("ID:", id, type(id))
    #     result = cur.execute("SELECT TotalCreditHours FROM Student WHERE StudentID = %s ", [id])
    #     cur.close()
    #     details = (result)
    #     print(details)
        
    return render_template("home.html", session = session)
