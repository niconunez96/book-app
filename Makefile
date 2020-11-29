.EXPORT_ALL_VARIABLES:
export ENV_CONFIG = settings.settings.DevelopmentConfig

runserver:
	python ./project/server.py
