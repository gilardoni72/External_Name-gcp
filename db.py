import os
from app import app
from flaskext.mysql import MySQL

mysql = MySQL()

# MySQL configurations y variables de  Kubernetes
app.config['MYSQL_DATABASE_USER'] = os.getenv('DB_USERNAME')
app.config['MYSQL_DATABASE_PASSWORD'] = os.getenv('DB_PASSWORD')
app.config['MYSQL_DATABASE_DB']  = os.getenv('DB_NAME')
app.config['MYSQL_DATABASE_HOST'] = os.getenv('DB_HOSTNAME')
mysql.init_app(app)
