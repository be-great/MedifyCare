from flask import render_template
from flask_login import login_required, current_user
from flask import Blueprint
from flask_socketio import emit, join_room
from webapp import socketio
from .chat_controller import save_message

chat_blueprint = Blueprint(
    'chat',
    __name__,
    template_folder='../templates/chat',
    url_prefix="/chat"
)


@chat_blueprint.route('/room', methods=['GET'])
@login_required
def chat_room():
    return render_template('chat_room.html')

@socketio.on('send_message')
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
