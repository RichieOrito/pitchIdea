import os

class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST = 'app/static/img'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    
    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SUBJECT_PREFIX = 'pitchIdea'
    SENDER_EMAIL = 'richard.omondi@student.moringaschool.com'

    # Flask-User settings
    USER_APP_NAME = "pitchIdea"
    USER_ENABLE_EMAIL = True
    USER_ENABLE_USERNAME = True
    USER_EMAIL_SENDER_NAME = USER_APP_NAME

    #simple mde configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    DEBUG = True

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL')