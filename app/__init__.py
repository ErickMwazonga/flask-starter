from flask import Flask 
from flask_bootstrap import Bootstrap 
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy 
from dotenv import load_dotenv

from config import config

# register third-party apps
bootstrap = Bootstrap()
moment = Moment()
db = SQLAlchemy()
load_dotenv()

def create_app(config_name):
    app = Flask(__name__, template_folder='templates') 
    
    app.config.from_object(config[config_name]) 
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    moment.init_app(app)
    db.init_app(app)

    # Register context processor
    @app.context_processor
    def inject_app_title():
        return dict(app_name=app.config['APP_NAME'])

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
