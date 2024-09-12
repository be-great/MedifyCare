# from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from .. import db


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    receiver_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    video_call_id = db.Column(db.String(255))
    is_video_call = db.Column(db.Boolean, default=False)
