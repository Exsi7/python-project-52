runserver:
		poetry run python manage.py runserver
start:
	poetry run gunicorn --workers=5 python-project-52.task_manager.wsgi
makerequirements:
	poetry export --without-hashes --format=requirements.txt > requirements.txt