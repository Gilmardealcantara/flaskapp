from flask.ext.wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

class LoginForm(Form):
    firstName = StringField('firstName', validators=[DataRequired()])
    lastName = StringField('lastName', validators=[DataRequired()])
    phone = StringField('phone', validators=[DataRequired()])