import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    APP_NAME = os.getenv('APP_NAME', 'Flask App')
    
    SECRET_KEY = os.getenv('SECRET_KEY', 'RANDOMNESS')

    # MySQL configurations
    MYSQL_HOST = os.getenv('MYSQL_HOST')
    MYSQL_USER = os.getenv('MYSQL_USER')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
    MYSQL_DB = os.getenv('MYSQL_DB')

    # SQLAlchemy configurations
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config): 
    DEBUG = True
    SQLITE_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or SQLITE_DATABASE_URI

class TestingConfig(Config): 
    ...

class ProductionConfig(Config):
    ...


config = {
    'default': DevelopmentConfig,
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}

