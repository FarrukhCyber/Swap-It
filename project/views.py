from flask import Blueprint, render_template, request, flash, jsonify
from .db_config import create_db
from flask_login import login_required, current_user


mysql = create_db()

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home_page():
    return render_template("home.html")
