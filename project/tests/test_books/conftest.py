import pytest
from werkzeug.utils import import_string

from server import app
from database import db


@pytest.fixture
def app_test():
    config_class = import_string("settings.settings.TestingConfig")()
    app.config.from_object(config_class)
    app.config['SQLALCHEMY_DATABASE_URI'] = config_class.DATABASE_URI
    yield app


@pytest.fixture()
def db_test(app_test):
    app_test.app_context().push()
    db.init_app(app_test)
    db.create_all()
    yield db
    db.session.close()
    db.drop_all()
