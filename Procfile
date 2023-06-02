web:  poetry run gunicorn task_manager.wsgi --log-file -
release: poetry run python manage.py collectstatic && python manage.py migrate