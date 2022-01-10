from flask import Flask
from flaskapp.routes import items


def create_app():
    app = Flask(__name__, static_folder='build/', static_url_path='/')

    app.register_blueprint(items)
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///database.db'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = 'secret_key'

    from flaskapp.db import db
    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app
