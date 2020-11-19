from flask import Flask


app = Flask(__name__)


from project.controller import books  # noqa
