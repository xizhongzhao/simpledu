from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.valitators import Length,Email,EqualTo,Required

class RegisterForm(FlaskForm):
    username = StringField('username',validators=[Required(),Length(3,24)])
    email = StringField('email',validators=[Required(),Length(6,24)])
    password = PasswordField('password',validators=[Required(),length(6,24)])
    repeat_password = ('repeat password',validators=[Required(),EqualTo('password')])
    submit = SubmitField('sumit')

class Login
