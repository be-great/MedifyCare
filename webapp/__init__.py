from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
db = SQLAlchemy()
migrate = Migrate()


def create_app(object_name):
 
    app = Flask(__name__)
    app.config.from_object(object_name)
    db.init_app(app)
    migrate.init_app(app, db)

    from .main import main_create_module
    from .auth import auth_create_module
    main_create_module(app)
    auth_create_module(app)
    return app

