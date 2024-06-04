from datetime import datetime
from . import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String(64), unique=True)
    created_at = db.Column(db.Date, default=datetime.now())

    def __repr__(self):
        return f'<User: {self.name}>'
    
