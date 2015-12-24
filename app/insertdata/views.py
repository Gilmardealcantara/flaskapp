from app import app, conn
from flask import render_template, request, Blueprint, g
from forms import LoginForm

mod = Blueprint('insertdata', __name__, url_prefix='/<lang_code>/insertdata')

@mod.url_defaults
def add_language_code(endpoint, values):
    values.setdefault('lang_code', g.lang_code)

@mod.url_value_preprocessor
def pull_lang_code(endpoint, values):
    g.lang_code = values.pop('lang_code')

@mod.route('/', methods=['GET', 'POST'])
def insertdata():
    if request.method == 'POST':
        form = LoginForm()
        if form.validate_on_submit():
            fields = ('firstName', 'lastName', 'phone')
            firstName = str(form.firstName.data)
            lastName = str(form.lastName.data)
            phone = str(form.phone.data)
            
            connection =  conn()
            cursor = connection.cursor()
            cursor.execute("INSERT INTO users (firstName, lastName, phone) VALUES ('%s', '%s', '%s')" % (firstName, lastName, phone))
            connection.commit()
            
            flash('Dados inseridos com sucesso! First Name = "%s", Last Name = "%s", Phone = "%s"' % (firstName, lastName, phone))
            return redirect('/insertdata')
        return render_template('insertdata/index.html', form=form)
    return render_template('insertdata/index.html', form=LoginForm())