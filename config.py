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
    SQLALCHEMY_DATABASE_URI = 'postgres://lqeiipmerxmova:57187b08eee8f9cf3a474bc19c4a096de26286fb574109e9fe04bf46af7e5515@ec2-34-233-157-189.compute-1.amazonaws.com:5432/d1lmlnudcaqafe'
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