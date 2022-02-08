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
    SQLALCHEMY_DATABASE_URI = 'postgresql://yjepbvpegfavnq:e1df0aa42c22269a1a0816d05da770fa233ef7fc52926f6f077c12325cd85863@ec2-23-20-73-25.compute-1.amazonaws.com:5432/d6sn6p68ltghk5'
    pass

class DevConfig(Config):

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:xoxo@localhost/pitch'
    
    DEBUG = True


class TestConfig(Config):
    pass    


config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig

}