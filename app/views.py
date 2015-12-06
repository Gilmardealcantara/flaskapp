from flask import jsonify, render_template, request, flash, redirect
from app import app
import MySQLdb
from .form import LoginForm
import collections
app.config["JSON_SORT_KEYS"] = False

conn = MySQLdb.connect(host='localhost', user='root', passwd='', db='flaskapp')
cursor = conn.cursor()

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/insertdata', methods=['GET', 'POST'])
def insertdata():
    if request.method == 'POST':
        form = LoginForm()
        if form.validate_on_submit():
            fields = ('firstName', 'lastName', 'phone')
            firstName = str(form.firstName.data)
            lastName = str(form.lastName.data)
            phone = str(form.phone.data)
            values = (firstName,lastName,phone)
        
            print fields
            print values

            cursor.execute("INSERT INTO users (firstName, lastName, phone) VALUES ('a', 'b','c')")
            conn.commit()

#        def insert(table, fields=(), values=()):
#            query = 'INSERT INTO %s (%s) VALUES (%s)' % (
#                table,
#                ', '.join(fields),
#                ', '.join(values)
#            )
#
#            print query
#            cursor.execute(query, values)
#            cursor.commit()
#
#        insert('users', fields, values)
#        #conn.commit()
        
        #cursor.execute("SELECT id, firstName, lastName, phone FROM users")
        #rows = cursor.fetchall()
        #print rows
            flash('Dados inseridos com sucesso firstName="%s", lastName="%s", phone="%s"' % (form.firstName.data, form.lastName.data, form.phone.data))
            return redirect('/insertdata')
        return render_template('insertdata.html', form=form)
    return render_template('insertdata.html', form=LoginForm())

@app.route('/showdata', methods=['GET'])
def showdata():
        cursor.execute("SELECT id, firstName, lastName, phone FROM users")
        rows = cursor.fetchall()
        objects_list = []
        for row in rows:
            d = collections.OrderedDict()
            d['id'] = row[0]
            d['firstName'] = row[1]
            d['lastName'] = row[2]
            d['phone'] = row[3]
            objects_list.append(d)
            return render_template('showdata.html'),jsonify(dados=objects_list, sort_keys=False) 

@app.route('/about')
def about():
    return render_template('about.html')
