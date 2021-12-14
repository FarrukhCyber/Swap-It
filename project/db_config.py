from . import app
from flask_mysqldb import MySQL 

# MYSQL DB configuartions
def create_db():
    app.config['MYSQL_HOST'] = 'us-cdbr-east-05.cleardb.net'
    app.config['MYSQL_USER'] = 'bb29c37c5803df'

    app.config['MYSQL_PASSWORD'] = '9fc3e4c6'
    app.config['MYSQL_DB'] = 'heroku_58cd6fc93d90184'
    mysql = MySQL(app)
    
    return mysql