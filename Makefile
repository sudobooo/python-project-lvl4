install:
	poetry install

lint:
	poetry run flake8 task_manager

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=task_manager --cov-report xml

migrate:
	poetry run python manage.py makemigrations
	poetry run python manage.py migrate

push_heroku:
	poetry export -f requirements.txt --output requirements.txt
	poetry run python manage.py collectstatic
	heroku run python manage.py makemigrations
	heroku run python manage.py migrate

runserver:
	poetry run python manage.py runserver 127.0.0.1:8000

transprepare:
	poetry run django-admin makemessages

transcompile:
	poetry run django-admin compilemessages
