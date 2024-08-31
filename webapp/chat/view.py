from flask import render_template
from flask_login import login_required, current_user
from flask import Blueprint
from flask_socketio import emit, join_room
from webapp import socketio
from .chat_controller import save_message
from ..auth.models import User, Role
from .. import db

chat_blueprint = Blueprint(
    'chat',
    __name__,
    template_folder='../templates/chat',
    url_prefix="/chat"
)


@chat_blueprint.route('/', methods=['GET'])
@login_required
def chat_room():
    doctors = db.session.query(
        User.username,
        User.specialty,
        User.bio,
        # User.is_available  # Assuming you have a field for availability
    ).join(User.roles).filter(Role.name == 'doctor').all()
    return render_template('chat_home.html', doctors=doctors)


@chat_blueprint.route('/consult/<username>', methods=['GET'])
@login_required
def consult_doc(username):
    # Fetch doctor details based on username

    doctor = User.query.filter_by(username=username).first_or_404()

    # Render the chat page with the doctor's details
    return render_template('consult_doc.html', doctor=doctor)


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
