runserver:
		poetry run python manage.py runserver
start:
	poetry run gunicorn -w 5 -b 0.0.0.0:8000 task_manager.wsgi