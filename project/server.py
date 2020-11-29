from flask import Flask
from werkzeug.utils import import_string
from controller.books import books
import os


def create_application(settings):
    config_class = import_string(settings)()
    app = Flask(__name__)
    app.config.from_object(config_class)
    # include endpoints
    app.register_blueprint(books)
    return app


if __name__ == "__main__":
    app = create_application(os.environ.get("ENV_CONFIG"))
    app.run(host="0.0.0.0", port=5000)
