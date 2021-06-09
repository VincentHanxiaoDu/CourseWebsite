from flask_sqlalchemy import SQLAlchemy

class Config:
    DEBUG = False
    SECRET_KEY = b'SECRET_KEY'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///webDB.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

db = SQLAlchemy()