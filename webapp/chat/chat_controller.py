from .models import db, Message
from flask_login import current_user

def save_message(receiver_id, content):
    message = Message(sender_id=current_user.id, receiver_id=receiver_id, content=content)
    db.session.add(message)
    db.session.commit()
    return message
