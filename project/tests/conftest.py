import pytest
from werkzeug.utils import import_string

from server import app
from database import db


@pytest.fixture
def app_test():
    setting = "settings.settings.TestingConfig"
    config = import_string(setting)()
    app.config.from_object(config)
    app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_URI
    # silence the deprecation warning
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    yield app


@pytest.fixture
def client(app_test):
    with app_test.test_client() as client:
        with app_test.app_context():
            db.drop_all()
            db.create_all()
        yield client


@pytest.fixture()
def db_test(app_test):
    app_test.app_context().push()
    db.init_app(app_test)
    db.create_all()
    yield db
    db.session.close()
    db.drop_all()
