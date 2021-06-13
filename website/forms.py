
from threading import current_thread
from flask_wtf import FlaskForm
from sqlalchemy.sql.sqltypes import String
from wtforms.fields import TextAreaField,SubmitField, StringField, PasswordField
from wtforms.fields.core import IntegerField
from wtforms.validators import InputRequired, Length, Email, EqualTo
from wtforms.widgets.core import CheckboxInput


#creates the login information
class LoginForm(FlaskForm):
    user_name=StringField("User Name", validators=[InputRequired('Enter user name')])
    password=PasswordField("Password", validators=[InputRequired('Enter user password')])
    submit = SubmitField("Login")

 # this is the registration form
class RegisterForm(FlaskForm):
    user_name=StringField("User Name", validators=[InputRequired()])
    email_id = StringField("Email Address", validators=[Email("Please enter a valid email")])
    
    #add buyer/seller - check if it is a buyer or seller hint : Use RequiredIf field


    #linking two fields - password should be equal to data entered in confirm
    password=PasswordField("Password", validators=[InputRequired(),
                  EqualTo('confirm', message="Passwords should match")])
    confirm = PasswordField("Confirm Password")

    # sets admin to 0
    submitCustomer = SubmitField("Register As Customer")

    # sets admin to 1
    submitAdmin = SubmitField("Register As Admin")

class EventsForm(FlaskForm):
    name = StringField('Evemt', validators=[InputRequired()])
    description = TextAreaField('Description', validators=[InputRequired()])
    image = StringField('Cover Image', validators=[InputRequired()])
    date = StringField('Event Date', validators=[InputRequired()])
    status = StringField('Event Status', validators=[InputRequired()])
    ticketQTY = IntegerField('Ticket Quantity', validator=[InputRequired])
    submit = SubmitField("Create")

class CommentForm(FlaskForm):
    text = TextAreaField('Comment', [InputRequired()])
    submit = SubmitField('Create')