.EXPORT_ALL_VARIABLES:
export ENV_CONFIG = settings.settings.DevelopmentConfig
export DB_CONNECTOR=mysql+mysqlconnector
export DB_USER=nicolas
export DB_PASS=39853201
export DB_HOST=localhost
export DB_NAME=book_db

run_migrations:
	python ./project/manage.py db init
	python ./project/manage.py db migrate
	python ./project/manage.py db upgrade

runserver:
	python ./project/server.py

update_requirements:
	pip freeze | grep -v 0.0.0 > requirements.txt