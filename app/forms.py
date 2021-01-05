from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, SubmitField, BooleanField, validators
from wtforms.validators import DataRequired, EqualTo,Length, Email
import email_validator


class SignupForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(),Length(min=5, message='Must be longer than 4 characters')])
    email = StringField('Email',
                        validators=[DataRequired(), Email(message='Enter a valid email')])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8,message='Use a stronger passowrd')])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password' ,message='Passwords must match')])
    submit_button = SubmitField('Sign Up')


class SigninForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Stay signed in')
    submit_button = SubmitField('Sign in')

class ForgotPasswordForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])

class ResetForm(FlaskForm):
    old_password= PasswordField('Old Password', validators=[DataRequired(), Length(min=8)])

class PostForm(FlaskForm):
    title_of_post=StringField('Title for your post', validators=[DataRequired()])
    body=TextAreaField('Content for your post',validators=[DataRequired()])
    submit_button=SubmitField('Add Post')


