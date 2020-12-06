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
