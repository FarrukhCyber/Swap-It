from flask import Blueprint, render_template, request, flash, jsonify
from flask.helpers import url_for
from werkzeug.utils import redirect
from project.auth import session
from .db_config import create_db
from project import views

mysql = create_db()

drop = Blueprint('drop', __name__)


@drop.route('/drop', methods=['GET', 'POST'])
def drop_course():
    if request.method == "POST":
        print("inside POST IF")
        user_id = request.form.get("options")
        return f"<h1>user_id<h1>"

    else:
        user_id = session["user"][0]
        print("USer:", user_id)
        cur = mysql.connection.cursor()
        value = cur.execute("SELECT CourseID, SectionID FROM takes WHERE StudentID=%s", [user_id])
        result = cur.fetchall()
        # print(result)
        # return redirect(url_for('views.home_page'))
        print("I'm going to return")
        return render_template("drop.html", data= result)
        # cur.close()
        # try:
        #     try:
        #         cur.execute("SELECT CourseID, SectionID FROM takes WHERE StudentID=%s", [user_id])
        #     # NB : you won't get an IntegrityError when reading
        #     except (MySQLdb.Error, MySQLdb.Warning) as e:
        #         print(e)
        #         return e
        #     try:
        #         result = cur.fetchall()
        #         return result
        #     except TypeError as e:
        #         print(e)
        #         return e

        # finally:
        #     cur.close()
            
