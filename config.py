
class Config(object):
    DEBUG = True
    SECRET_HERE = 'dasdasdasdsadss'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///movies.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_AS_ASCII = False
    RESTX_JSON = {'ensure_ascii': False, 'indent': 3}
    HOST = "localhost"
    PORT = 10001
