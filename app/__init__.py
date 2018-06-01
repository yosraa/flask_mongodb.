import os
from flask import Flask
from app.model.user import db, User


def create_app(script_info=None):

    # instantiate the app
    app = Flask(__name__, template_folder='', static_folder='')

    # set config
    app_settings = os.getenv('APP_SETTINGS', 'app.config.DevelopmentConfig')
    app.config.from_object(app_settings)
    # Setup the database.
    db.init_app(app)
    User.objects.create(email='yosraaddali@gmail.com')

    # set up extensions
    from app.app_api import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')
    return app