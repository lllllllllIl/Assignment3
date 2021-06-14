from flask import Blueprint, render_template, request, session, redirect, url_for
from sqlalchemy.sql.sqltypes import NullType
from .models import Events, Users
from . import db

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    events = Events.query.all()

    return render_template('index.html', events=events)


@bp.route('/eventCreation.html')
def eventCreation():

    return render_template('eventCreation.html')

@bp.route('/eventDetails.html')
def eventDetails():
    return render_template('eventDetails.html', Events=Events)

@bp.route('/login.html', methods=['GET', 'POST'])
def login():
    
    email = request.values.get('email')
    pwd = request.values.get('pwd')
    phone = request.values.get('phone')

    session['email'] = email

    return render_template('login.html')


@bp.route('/new_booking', methods=['GET','POST'])
def new_booking():
    form = bookForm(request.form)
    if request.method== 'post' and form.validate():
        booking = booking()
