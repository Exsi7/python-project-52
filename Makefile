runserver:
		poetry run python manage.py runserver
start:
	poetry run gunicorn --workers=5 task_manager.wsgi --log-file
makerequirements:
	poetry export --without-hashes --format=requirements.txt > requirements.txt