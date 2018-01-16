from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.valitators import Length,Email,EqualTo,Required

class RegisterForm(FlaskForm):
    username = StringField('username',validators=[Required(),Length(3,24)])
    email = StringField('email',validators=[Required(),Email(message = 'please input corecctor email!')])
    password = PasswordField('password',validators=[Required(),length(6,24)])
    repeat_password = PasswordField('repeat password',validators=[Required(),EqualTo('password')])
    submit = SubmitField('sumit')

class LoginForm(FlaskForm):
    email = StringField('email',validators = [Required(),Email(message='please input corecctor email!')])
    password = PasswordField('password',validators=[Required(),Length(6,24)])
    remember_me = BooleanField('remember me!')
    sumit = SubmitField('summit')
