from flask import Blueprint, render_template, request, flash, jsonify
from .db_config import create_db

mysql = create_db()

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return "LOGIN"


@auth.route('/logout')
def logout():
    return "LOGOUT"

@auth.route('/signup', methods=['GET', 'POST'])
def sign_up():
    return "SIGN UP"