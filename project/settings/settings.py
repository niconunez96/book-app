class Config(object):
    DEBUG = False
    TESTING = False
    # DATABASE_URI = 'sqlite:///:memory:'


class ProductionConfig(Config):
    ENV = "production"
    DATABASE_URI = 'mysql://user@localhost/foo'


class DevelopmentConfig(Config):
    ENV = "development"
    DEBUG = True
    DATABASE_URI = 'postgresql://dev_user:1234@db_server:5432/book_db'


class TestingConfig(Config):
    ENV = "testing"
    TESTING = True
    DEBUG = True
