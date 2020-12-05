import os
from flask import Flask
from database import db
from werkzeug.utils import import_string
from controller import (
    books as book_endpoints,
    authors as author_endpoints,
)


settings = os.environ.get("ENV_CONFIG")
config_class = import_string(settings)()
app = Flask(__name__)
app.config.from_object(config_class)
# include endpoints
app.register_blueprint(book_endpoints)
app.register_blueprint(author_endpoints)
app.config['SQLALCHEMY_DATABASE_URI'] = config_class.DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # silence the deprecation warning
db.init_app(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
