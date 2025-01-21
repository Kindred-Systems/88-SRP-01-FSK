import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'fallback_secret_key')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///fallback.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
