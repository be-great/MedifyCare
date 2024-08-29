from flask_socketio import emit, join_room
from . import chat_blueprint
from chat_controller import save_message
from flask_login import current_user, login_required

@chat_blueprint.socketio.on('send_message')
@login_required
def handle_send_message(data):
    message = save_message(data['receiver_id'], data['message'])
    emit('receive_message', {'message': message.content, 'sender_id': message.sender_id}, room=data['receiver_id'])

# @chat_blueprint.socketio.on('join')
# @login_required
# def handle_join(data):
#     """remeber to edit this code so it will display message request instead"""
#     join_room(data['room'])
#     emit('status', {'msg': current_user.username + ' has joined the room.'}, room=data['room'])
