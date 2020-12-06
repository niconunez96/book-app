import pytest

import server
from server import AppBuilder
from database import db


@pytest.fixture
def app_test():
    setting = "settings.settings.TestingConfig"
    app_builder = AppBuilder(server.__name__, setting)
    app_builder.add_database()
    yield app_builder.build()


@pytest.fixture()
def db_test(app_test):
    app_test.app_context().push()
    db.init_app(app_test)
    db.create_all()
    yield db
    db.session.close()
    db.drop_all()
