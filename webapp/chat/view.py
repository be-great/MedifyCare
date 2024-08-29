from flask import render_template
from flask_login import login_required
from . import chat_blueprint

@chat_blueprint.route('/room', methods=['GET'])
@login_required
def chat_room():
    return render_template('tempates/chat/chat_room.html')
