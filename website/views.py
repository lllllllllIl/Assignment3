from flask import Blueprint, render_template, request, session, redirect, url_for
from .models import events


bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    Event = events.query.all()

    return render_template('index.html', Event = events)

@bp.route('/EventCreation')
def eventCreation():

    return render_template('eventCration.html')

@bp.route('/EventDetails')
def eventDetails():
    return render_template('eventDetails.html')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    #if 'email' in session:
    #   return redirect('/')
    
    email = request.values.get('email')
    pwd = request.values.get('pwd')
    phone = request.values.get('phone')

    session['email'] = email

    return render_template('login.html')

@bp.route('/logout')
def logout():
    if 'email' in session:
        session.pop('email', None)
    return 'Session has been cleared'