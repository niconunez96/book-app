.EXPORT_ALL_VARIABLES:
export ENV_CONFIG = settings.settings.DevelopmentConfig
export DB_CONNECTOR=mysql+mysqlconnector
export DB_USER=nicolas
export DB_PASS=39853201
export DB_HOST=localhost
export DB_NAME=book_db

create_migrations:
	python ./project/manage.py db init
	python ./project/manage.py db migrate

update_requirements:
	pip freeze | grep -v 0.0.0 > requirements.txt

server-logs:
	docker logs -f book-app

runserver:
	docker-compose up --build -d

stopserver:
	docker-compose down
