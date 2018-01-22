from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,ValidationError
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
    
    def validate_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('name is exists')
    
    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('email is exists')

class LoginForm(FlaskForm):
    email = StringField('email',validators = [Required(),Email(message='please input corecctor email!')])
    password = PasswordField('password',validators=[Required(),Length(6,24)])
    remember_me = BooleanField('remember me!')
    submit = SubmitField('submit')

    def validate_email(self,field):
        if field.data and not User.query.filter_by(email=field.data).first():
            raise ValidationError('email is not register')
    
    def validate_password(self,field):
        user = User.query.filter_by(email=self.email.data).first()
        if user and not user.check_password(field.data):
            raise ValidationError('password is wrong')


class NameForm(FlaskForm):
    name = StringField('name')

    def validate_name(self,field):
        if len(field.data) < 2:
            raise ValidationError('Length of name can not less than 2')
