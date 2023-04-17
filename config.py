import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "your_secret_key_here"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or \
        f"mysql+pymysql://root:@127.0.0.1:3306/SeamlesGPT"
    SQLALCHEMY_TRACK_MODIFICATIONS = False