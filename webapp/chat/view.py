from flask import render_template
from flask_login import login_required, current_user
from flask import Blueprint
from flask_socketio import emit, join_room
from webapp import socketio
from ..auth.models import User, Role
from .chat_controller import save_message, get_messages
from .. import db
from .models import Message

chat_blueprint = Blueprint(
    'chat',
    __name__,
    template_folder='../templates/chat',
    url_prefix="/chat"
)


@chat_blueprint.route('/', methods=['GET'])
@login_required
def my_doctor():
    doctors = db.session.query(
        User.username,
        User.specialty,
        User.bio,
        # User.is_available  # Assuming you have a field for availability
    ).join(User.roles).filter(Role.name == 'doctor').all()
    return render_template('patient_home.html', doctors=doctors)


@chat_blueprint.route('/patients', methods=['GET'])
@login_required
def my_patients():
    # Fetch the list of patients who have sent messages to the doctor
    patients = User.query.join(
        Message,
        (Message.sender_id == User.id) & (Message.receiver_id == current_user.id)
    ).join(Role, User.roles).filter(Role.name == 'patient').distinct().all()

    return render_template('doc_home.html', patients=patients)


@chat_blueprint.route('/consult/<username>', methods=['GET'])
@login_required
def consult_doc(username):
    # Fetch doctor details based on username
    doctor = User.query.filter_by(username=username).first_or_404()

    # fetch old messages
    messages = get_messages(current_user.id, doctor.id)

    # Render the chat page with the doctor's details
    return render_template('consult_doc.html', doctor=doctor, messages=messages)


@socketio.on('join_room')
@login_required
def handle_join_room(room):
    join_room(room)
    emit('status', {'msg': current_user.username
                    + ' has entered the room.'}, room=room)


@socketio.on('connect')
def handle_connect():
    print(f"{current_user.username} connected.")

@socketio.on('disconnect')
def handle_disconnect():
    print(f"{current_user.username} disconnected.")


@socketio.on('send_message')
@login_required
def handle_send_message(data):
    # Assume the room name format is "<doctor_username>_<patient_username>"
    room = data['room']
    # Extract the doctor username (or adjust as per your room naming logic)
    doctor_username = room.split('_')[0]

    # Get the receiver ID (doctor's ID)
    doctor = User.query.filter_by(username=doctor_username).first()
    if doctor:
        # Save the message using the save_message function from chat_controller.py
        message = save_message(receiver_id=doctor.id, content=data['message'])

        # Emit the message to the room with additional details
        emit('receive_message', {
            'user': current_user.username,
            'message': message.content,  # Using message.content from the saved message
            'timestamp': message.timestamp.strftime('%Y-%m-%d %H:%M:%S')  # Send timestamp if needed
        }, room=room)
    else:
        # Handle case where doctor is not found
        emit('error', {'msg': 'Doctor not found'}, room=room)
