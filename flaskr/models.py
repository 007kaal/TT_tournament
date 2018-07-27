from datetime import datetime
from flask import Flask, current_app as app
from flask_sqlalchemy import SQLAlchemy
import enum
import mysqlclient-python.MySqldb

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:Bnmghj321#@localhost/TT"
db = SQLAlchemy(app)

class MatchType(enum.Enum):
     W_SINGLE = 'WS'
     M_SINGLE = 'MS'
     M_DOUBLE = 'MD'
     W_DOUBLE = 'WD'
     MIX_DOUBLE ='XD'


class matches(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    team1 = db.Column(db.Integer, nullable=False)
    team2 =  db.Column(db.Integer, nullable=False)
    round =  db.Column(db.Integer, nullable=False)
    next = db.Column(db.Integer)
    category = db.Column(db.Enum(MatchType))
    winner = db.Column(db.Integer, default = 0, nullable=False)
    time = db.Column(db.TIMESTAMP(timezone = False), default=datetime.now(), nullable=False)

    def __repr__ (self):
      return "{O} : {1} vs {2}".format(self.id, self.team1, self.team2)

class teams(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    name1 = db.Column(db.String(100), nullable=False, default="")
    email1= db.Column(db.String(100), nullable=False, default="")
    phone1= db.Column(db.String(100))
    name2 = db.Column(db.String(100), nullable=False, default="")
    email2= db.Column(db.String(100), nullable=False, default="")
    phone2= db.Column(db.String(100))
    type  = db.Column(db.Enum(MatchType))

    def __repr__(self):
      if self.type == 'WS' or self.type == 'MS':
        return "{0} - {1}".format(self.id ,self.name1)
      else:
        return "{0} - {1}, {2}".format(self.id , self.name1, self.name2)



team = teams(name1 = "rohit", email1 = "a@gmail.com", phone1 = 22322, name2 = "jindal", email2 = "b@gmail.com", phone2 = 987255678, type = 'MD')

db.session.add(team)
db.session.commit()

