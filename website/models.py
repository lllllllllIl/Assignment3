### this would go into a models.py or something similar ###
from . import db
#We use ev_ent because event is a used term
from datetime import datetime
from sqlalchemy.types import Boolean

class User(db.Model):
    __tablename__='Users' # good practice to specify table name
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True, nullable=False)
    emailid = db.Column(db.String(100), index=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    admin = db. Column(db.Boolean)

class events (db.Model):
    __tablename__='Events'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    description = db.Column(db.String(200))
    image = db.Column(db.String(400))
    date = db.Column(db.DateTime)

def __repr__(self): 
    return "<Name: {}>".format(self.name)

class booking (db.Model):
   __tablename__='Bookings'
   __table_args__ = {'extend_existing': True}

   event_id = db.Column(db.Integer, db.ForeignKey('Events.id') )
   price = db.Column(db.Integer)
   qty = db.Column(db.Integer)
   date = db.Column(db.DATE)
   bookid = db.Column(db.Integer, primary_key = True)

class comments (db.Model):
    __tablename__ ='Comments'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(400))
    created_at = db.Column(db.DateTime, default=datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey('Users.id'))
    event_id = db.Column(db.Integer,db.ForeignKey('Events.id'))
def __repr__(self):
    return "<Comment: {}>".format(self.text)



# class created (db.Model):
#      __tablename__ = 'Creted events'

#      __table_args__ = {'extend_existing': True}

#      event_id = db.Column(db.Integer, db.ForeignKey('Events.id'))
#      creator = db.Column(db.String)
#      Date_Created= db.Column(db.DateTime, default=datetime.now())

# class created (db.Model):
#      __tablename__ = 'Creted events'
#      event_id = db.Column(db.Integerm, db.ForeignKey('Events.id'))
#      creator = db.Column(db.String)
#      Date_Created= db.Column(db.DateTime, default=datetime.now())

