
class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///placement_application.sqlite3'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "this is my project"
    JSON_SORT_KEYS = False