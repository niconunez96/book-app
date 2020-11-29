import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import import_string
from controller.books import books


settings = os.environ.get("ENV_CONFIG")
config_class = import_string(settings)()
app = Flask(__name__)
app.config.from_object(config_class)
# include endpoints
app.register_blueprint(books)
app.config['SQLALCHEMY_DATABASE_URI'] = config_class.DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # silence the deprecation warning
db = SQLAlchemy(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
