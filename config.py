class Config(object):
    PWD_HASH_SALT = b'secret here'
    PWD_HASH_ITERATIONS = 100_000
    SECRET = SECRET_HERE = '249y823r9v8238r9u'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///movies.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_AS_ASCII = False
