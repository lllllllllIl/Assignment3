from . import db
from datetime import datetime
from sqlalchemy.types import Boolean
from flask_login import UserMixin


class Users(db.Model, UserMixin):
    __tablename__='Users'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True, nullable=False)
    emailid = db.Column(db.String(100), index=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    admin = db. Column(db.Boolean)
    comments = db.relationship('Comments', backref='user')

class Events (db.Model):
    __tablename__='Events'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    description = db.Column(db.String(200))
    image = db.Column(db.String(400))
    date = db.Column(db.String(10))
    ticketQTY = db.Column(db.Integer) 
    status = db.Column(db.String(20))
    comments = db.relationship('Comments', backref='event')

def __repr__(self): 
    return "<Name: {}>".format(self.name)

class Bookings (db.Model):
   __tablename__='Bookings'
   __table_args__ = {'extend_existing': True}

   event_id = db.Column(db.Integer, db.ForeignKey('Events.id') )
   price = db.Column(db.Integer)
   qty = db.Column(db.Integer)
   date = db.Column(db.DATE)
   bookid = db.Column(db.Integer, primary_key = True)

class Comments (db.Model):
    __tablename__ ='Comments'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(400))
    created_at = db.Column(db.DateTime, default=datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey('Users.id'))
    event_id = db.Column(db.Integer,db.ForeignKey('Events.id'))
def __repr__(self):
    return "<Comment: {}>".format(self.text)

