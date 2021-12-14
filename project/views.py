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
    id = session["user"][0]
    cur = mysql.connect.cursor()
    cur.execute("SELECT TotalCreditHours FROM Student WHERE StudentID = %s ", [id])
    crd_hrs = cur.fetchall()
    crd_hrs = crd_hrs[0][0]
    cur.execute("SELECT * FROM takes WHERE StudentID = %s ", [id])
    result = cur.fetchall()
    no_courses = len(result)
    cur.close()
        
    return render_template("home.html", session = session, crd_hrs=crd_hrs, no_courses= no_courses)
