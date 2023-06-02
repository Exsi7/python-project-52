web:  poetry gunicorn task_manager.wsgi --log-file -
release: poetry python manage.py collectstatic && python manage.py migrate