from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_swagger_ui import get_swaggerui_blueprint
import logging
import os
from .models import db

def create_app():
    app = Flask(__name__, static_folder='static', static_url_path='/static')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///bookhub.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Logging setup
    app.logger.setLevel(logging.INFO)

    db.init_app(app)

    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Swagger UI
    SWAGGER_URL = '/docs'
    API_URL = '/static/swagger.yaml'
    swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config={'app_name': "BookHub"})
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

    with app.app_context():
        db.create_all()
        app.logger.info("Database initialized.")

    return app, db