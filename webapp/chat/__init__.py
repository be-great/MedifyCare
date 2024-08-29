from flask import Blueprint

chat_blueprint = Blueprint('chat', __name__, url_prefix='/chat')

from . import routes, sockets

