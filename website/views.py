from flask import Blueprint, render_template, request, session, redirect, url_for
from sqlalchemy.sql.sqltypes import NullType
from .models import Events, Users
from . import db

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    Event = Events.query.all()

    return render_template('index.html', Event=Events)


@bp.route('/eventCreation.html')
def eventCreation():
    isAdmin = request.form.get('admin')
    if isAdmin == 0 or NullType:
        redirect(url_for('main.index'))

    return render_template('eventCreation.html')

@bp.route('/eventDetails.html')
def eventDetails():
    return render_template('eventDetails.html')

@bp.route('/login.html', methods=['GET', 'POST'])
def login():
    # if 'email' in session:
    #   return redirect('/')
    
    email = request.values.get('email')
    pwd = request.values.get('pwd')
    phone = request.values.get('phone')

    session['email'] = email

    return render_template('login.html')
