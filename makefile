PROJECT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
PYTHON_INTERPRETER = python3

# Test if python is installed
ifeq (,$(shell $(PYTHON_INTERPRETER) --version))
$(error "Python is not installed!")
endif

.PHONY: clean
clean:
	@find . -type f -name "*.py[co]" -delete
	@find . -type d -name "__pycache__" -delete
	@find . -type d -name ".tox" -exec rm -r "{}" +
	@find . -type d -name ".pytest_cache" -exec rm -r "{}" +


.PHONY: clean_migrations
clean_migrations: clean
	find . -path "*/migrations/*.py" -not -name "__init__.py" -not -path "./.venv/*" -not -path "./venv/*" -not -path "*/home/migrations/0001_create_database_views.py" -delete
	find . -path "*/migrations/*.pyc" -not -path "./.venv/*" -not -path "./venv/*" -not -path "*/home/migrations/0001_create_database_views.pyc" -delete
	-rm db.sqlite3


migrations:
	$(PYTHON_INTERPRETER) manage.py makemigrations
	$(PYTHON_INTERPRETER) manage.py migrate
	$(PYTHON_INTERPRETER) manage.py loaddata initial_data


install-pip-tools:
	$(PYTHON_INTERPRETER) -m pip install pip-tools


install-build:
	$(PYTHON_INTERPRETER) -m pip install build


compile_requirements: install-pip-tools install-build
	pip-compile --no-emit-index-url \
				--verbose \
				--generate-hashes \
				--output-file requirements.txt \
				--strip-extras \
				pyproject.toml

	echo "--constraint $(PROJECT_DIR)/requirements.txt" | \
	pip-compile \
		--verbose \
		--generate-hashes \
		--output-file requirements-dev.txt \
		--extra dev \
		pyproject.toml


requirements: compile_requirements
	$(PYTHON_INTERPRETER) -m pip install -r requirements-dev.txt &&\
	pre-commit install
	$(PYTHON_INTERPRETER) -m pip install -r requirements.txt


scss:
	sass gestao_ambiental/scss/volt.scss gestao_ambiental/static/css/volt.css

# generate a new django secret key and copy it to .env file in the form SECRET_KEY=...
django-secret-key:
	$(PYTHON_INTERPRETER) -c 'from django.core.management.utils import get_random_secret_key; print("SECRET_KEY=" + get_random_secret_key())' >> .env


env-vars: django-secret-key
	echo "DEBUG=True" >> .env


.PHONY: runserver
runserver:
	$(PYTHON_INTERPRETER) manage.py runserver --nostatic

collectstatic:
	$(PYTHON_INTERPRETER) manage.py collectstatic --noinput

.PHONY: newapp
newapp:
	mkdir apps/$(name)
	$(PYTHON_INTERPRETER) manage.py startapp $(name) apps/$(name)
