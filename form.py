from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, length, EqualTo, ValidationError
from model import Donor


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), length(min=2, max=20)])
    name = StringField('Name', validators=[DataRequired(), length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), length(min=2, max=20)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    # validation to check that we dont add same user name to our data base
    def validate_username(self, username):
        user = Donor.select().where(Donor.username == username.data)
        if user:
            raise ValidationError('That username is taken. Please choose different one')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), length(min=2, max=20)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class CreateForm(FlaskForm):
    donation = IntegerField('Donation', validators=[DataRequired()])
    submit = SubmitField('Add Donation')


class SingleUserForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), length(min=2, max=20)])
    submit = SubmitField('Show Donation')
