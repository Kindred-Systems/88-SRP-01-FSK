from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('gsrv.config.Config')

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    # Import and register blueprints
    from gsrv.routes import main
    from gsrv.auth import auth
    app.register_blueprint(main)
    app.register_blueprint(auth)

    with app.app_context():
        db.create_all()  # Automatically create database tables

    return app
