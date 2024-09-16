# from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from .. import db


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    receiver_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    phone_number = db.Column(db.String(20), nullable=False)
class PhoneNumber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    recipient_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.now())

    sender = db.relationship('User', foreign_keys=[sender_id], backref='sent_numbers')
    recipient = db.relationship('User', foreign_keys=[recipient_id], backref='received_numbers')