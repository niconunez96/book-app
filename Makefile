.EXPORT_ALL_VARIABLES:
export FLASK_APP = project/server.py
export FLASK_ENV = development
export FLASK_DEBUG = 1

runserver:
	flask run
