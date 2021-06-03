### this would go into a models.py or something similar ###
from . import db
#We use ev_ent because event is a used term
import datetime
class User(db.Model):
    __tablename__='users' # good practice to specify table name
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True, nullable=False)
    emailid = db.Column(db.String(100), index=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

class ev_ent (db.Model):
      __tablename__= 'Events'
      id = db.Column(db.Integer, primary_key=True)
      name = db.Column(db.String(80))
      description = db.Column(db.String(200))
      image = db.Column(db.String(400))
      date = db.Column(db.DateTime)
def __repr__(self): 
    return "<Name: {}>".format(self.name)

class booking (db.Model):
   __tablename__='Bookings'
   event_id = db.Column(db.Integer, db.ForeignKey('Events.id') )
   price = db.Column(db.Integer)
   qty = db.Column(db.Integer)
   date = db.Column(db.date)
   bookid = db.Column(db.Integer, priumary_key = True)
   user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

class comments (db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(400))
    created_at = db.Column(db.DateTime, default=datetime.now())
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    event_id = db.Column(db.Integer,db.ForeignKey('Events.id'))
def __repr__(self):
    return "<Comment: {}>".format(self.text)


class created (db.Model):
     __tablename__ = 'Creted events'
     event_id = db.Column(db.Integerm, db.ForeignKey('Events.id'))
     creator = db.Column(db.String)
     Date_Created= db.Column(db.DateTime, default=datetime.now())