from . import app
from flask_mysqldb import MySQL 

# MYSQL DB configuartions
def create_db():
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = '786@mf12'
    app.config['MYSQL_DB'] = 't2'
    mysql = MySQL(app)
    
    return mysql