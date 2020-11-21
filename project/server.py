from flask import Flask


app = Flask(__name__)

# include endpoints
from project.controller import books  # noqa


if __name__ == "__main__":
    app.run(host="127.0.0.1")
