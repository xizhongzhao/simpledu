from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import Length,Email,EqualTo,Required
from simpledu.models import db,User

class RegisterForm(FlaskForm):
    username = StringField('username',validators=[Required(),Length(3,24)])
    email = StringField('email',validators=[Required(),Email(message = 'please input corecctor email!')])
    password = PasswordField('password',validators=[Required(),Length(6,24)])
    repeat_password = PasswordField('repeat password',validators=[Required(),EqualTo('password')])
    submit = SubmitField('submit')
    
    def create_user(self):
        user = User()
        user.username = self.username.data
        user.email = self.email.data
        user.password = self.password.data
        db.session.add(user)
        db.session.commit()
        return user

class LoginForm(FlaskForm):
    email = StringField('email',validators = [Required(),Email(message='please input corecctor email!')])
    password = PasswordField('password',validators=[Required(),Length(6,24)])
    remember_me = BooleanField('remember me!')
    submit = SubmitField('submit')
