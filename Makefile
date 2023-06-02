runserver:
		poetry run python manage.py runserver
start:
	poetry run gunicorn task_manager.wsgi 
makerequirements:
	poetry export --without-hashes --format=requirements.txt > requirements.txt