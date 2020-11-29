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


class TestingConfig(Config):
    ENV = "testing"
    TESTING = True
    DEBUG = True
