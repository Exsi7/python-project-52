runserver:
		poetry run python manage.py runserver
start:
	poetry run gunicorn --workers=5 task_manager.wsgi