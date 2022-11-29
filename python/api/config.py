#config.py
import os
from os.path import dirname, abspath


base_dir =os.path.join(dirname(abspath(__file__)))



class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TEMPLATES_AUTO_RELOAD = True
    FLASK_DEBUG = 1
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir, 'db', 'database.db')
    print(SQLALCHEMY_DATABASE_URI)
    
    @staticmethod
    def init_app(app):
        pass

config = {
    "default": Config
}