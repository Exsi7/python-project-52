runserver:
		poetry run python manage.py runserver

makerequirements:
	poetry export --without-hashes --format=requirements.txt > requirements.txt

install:
		poetry install

makemigrations:
		poetry run python manage.py makemigrations

migrate: makemigrations
		poetry run python manage.py migrate

start: migrate
	poetry run gunicorn -w 5 -b 0.0.0.0:8000 task_manager.wsgi --log-file -

makemessages:
		poetry run django-admin makemessages -l ru

compilemessages:
		poetry run django-admin compilemessages

lint:
		poetry run flake8