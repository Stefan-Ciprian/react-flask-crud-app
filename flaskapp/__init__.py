from flask import Flask
from flaskapp.routes import items
from flaskapp.database import db_session


def create_app(config):
    app = Flask(__name__, static_folder='build/', static_url_path='/')

    app.register_blueprint(items)
    app.config['TESTING'] = config.TESTING

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()

    return app
