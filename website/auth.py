from flask import ( 
    Blueprint, flash, render_template, request, url_for, redirect
) 
from werkzeug.security import generate_password_hash,check_password_hash
from wtforms.fields.simple import PasswordField
from .forms import LoginForm, RegisterForm
from flask_login import login_user, login_required,logout_user
from website import db
from .models import Users
from flask import Flask, session
from flask_login import UserMixin



#create a blueprint
bp = Blueprint('auth', __name__)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    error=None
    if(login_form.validate_on_submit()==True):
        #get the username and password from the database
        user_name = login_form.user_name.data
        password = login_form.password.data
        u1 = Users.query.filter_by(name=user_name).first()
        #if there is no user with that name
        if u1 is None:
            error='Incorrect username' 
        #check the password - notice password hash function
        elif not check_password_hash(u1.password_hash, password): # takes the hash and password
            error='Incorrect password'
        if error is None:
            #all good, set the login_user of flask_login to manage the user
            login_user(u1)
            flash(f'Successfully logged in! Hello {u1.name}', 'success')
            return redirect(url_for('main.index'))
        else:
            flash(error)
    return render_template('user.html', form=login_form, heading='Login')

@bp.route('/register', methods=['GET', 'POST'])
def register():
    register = RegisterForm()
    #the validation of form submis is fine
    if (register.validate_on_submit() == True):
            #get username, password and email from the form
            uname = register.user_name.data
            pwd = register.password.data
            email=register.email_id.data
            _admin=register.submitAdmin.data #If button not pressed, returns 0
            #check if a user exists
            u1 = Users.query.filter_by(name=uname).first()
            if u1:
                flash('User name already exists, please login')
                return redirect(url_for('auth.login'))
            # don't store the password - create password hash
            pwd_hash = generate_password_hash(pwd)
            #create a new user model object
            new_user = Users(name=uname, password_hash=pwd_hash, emailid=email, admin=_admin)
            db.session.add(new_user)
            db.session.commit()
            flash(f'Successfully created account {new_user.name}!')
            #commit to the database and redirect to HTML page
            return redirect(url_for('main.index'))
    #the else is called when there is a get message
    else:
        return render_template('user.html', form=register, heading='Register')

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Successfully logged out')
    return redirect(url_for('main.index'))

#Creating the access and determining the acces controls
ACCESS = {
    'guest': 0,
    'user': 1,
    'admin': 2
}

class User():
    def __init__(self, name, email, password, access=ACCESS['user']):
        self.name = name
        self.email = email
        self.password = password
        self.access = access
    
    def is_admin(self):
        return self.access == ACCESS['admin']

    def allowed(self, access_level):
        return self.access >= access_level