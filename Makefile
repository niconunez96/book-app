.EXPORT_ALL_VARIABLES:
export ENV_CONFIG = settings.settings.DevelopmentConfig

runserver:
	python ./project/server.py

update_requirements:
	pip freeze | grep -v 0.0.0 > requirements.txt