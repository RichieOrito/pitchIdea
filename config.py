import os

class Config:

    SECRET_KEY = os.environ.get('SECRET_KEY')

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST ='app/static/photos'

    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SUBJECT_PREFIX = 'Pitch'
    SENDER_EMAIL = 'richard.omondi@student.moringaschool.com'

    #simple mde configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace("://", "ql://", 1)
    
    pass

class DevConfig(Config):

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE")
    
    DEBUG = True


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_TEST")
    pass    


config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig

}