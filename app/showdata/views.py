from app import app, conn
from flask import render_template, Blueprint, g
import collections

mod = Blueprint('showdata', __name__, url_prefix='/<lang_code>/showdata')

@mod.url_defaults
def add_language_code(endpoint, values):
    values.setdefault('lang_code', g.lang_code)

@mod.url_value_preprocessor
def pull_lang_code(endpoint, values):
    g.lang_code = values.pop('lang_code')

@mod.route('/', methods=['GET'])
def showdata():

    connection =  conn()
    cursor = connection.cursor()
    cursor.execute("SELECT id, firstName, lastName, phone FROM users")
    rows = cursor.fetchall()
    cursor.close()

    objects_list = []
    for row in rows:
        d = collections.OrderedDict()
        d['id'] = row[0]
        d['firstName'] = row[1]
        d['lastName'] = row[2]
        d['phone'] = row[3]
        objects_list.append(d)
    return render_template('showdata/index.html', dados=objects_list)