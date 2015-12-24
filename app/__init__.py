from flask import Flask
import MySQLdb

app = Flask(__name__)
app.config.from_object('config')
#app.config["JSON_SORT_KEYS"] = False

def conn():
	return MySQLdb.connect(host='localhost', user='root', passwd='', db='flaskapp')


''' views '''

from app.general.views import mod as general_module
from app.insertdata.views import mod as insertdata_module
from app.showdata.views import mod as showdata_module

app.register_blueprint(general_module)
app.register_blueprint(insertdata_module)
app.register_blueprint(showdata_module)
