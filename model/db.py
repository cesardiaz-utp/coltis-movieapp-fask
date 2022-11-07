from application import app
from flask_mysqldb import MySQL
from MySQLdb.cursors import Cursor

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'coltis_movie_flask'
app.config['MYSQL_PORT'] = 3306
mysql = MySQL(app)

def execute(sql: str) -> Cursor:
    cursor = mysql.connection.cursor()
    cursor.execute(sql)
    return cursor

def commit() -> None:
    mysql.connection.commit()