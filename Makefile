SHELL := /bin/bash
DOCKER ?= podman
DC ?= docker compose
DC_ARGS ?=
DC_BUILD_ARGS ?=
DC_PROD ?= $(DC) $(DC_ARGS) -f docker-compose.yml
DC_DEV ?= docker-compose $(DC_ARGS) -f docker-compose.dev.yml
DB_DUMP ?= ./streetnoise_cms.dump
dev-db-up:
	 $(DC_DEV) up -d

lint:
	flake8 --exclude "*migrations*,venv,node_modules" -v --max-line-length 999 .

fmt:
	black --exclude "(.*/migrations/.*|node_modules|.git)" .

dev-watch:
	npm run watch

dev-static:
	 python manage.py collectstatic --clear --noinput
	 python manage.py collectstatic --no-post-process --noinput

dev-serve:
	 python manage.py runserver 0.0.0.0:8001

dev-reset:
	$(DC_DEV) down
	$(DOCKER) volume rm cms_streetnoise_dev_db14
	$(DC_DEV) up -d
	sleep 10
	cat $(DB_DUMP) |  $(DOCKER) exec  -i cms-db-1 psql -U streetnoise_cms


serve: dev-migrate dev-serve

dev-makemigrations:
	python manage.py makemigrations

dev-db-load-dump:
	cat $(DB_DUMP) |  $(DOCKER) exec  -i cms-db-1 psql -U streetnoise_cms

dev-migrate: #dev-makemigrations
	python manage.py migrate
	python manage.py sync_page_translation_fields
	python manage.py update_translation_fields

dev-i18n:
	python manage.py makemessages -l de -i 'venv*'
	python manage.py compilemessages  -l de -i 'venv*'

dev-dump-db:
	$(DC_DEV) exec db pg_dump -U streetnoise_cms streetnoise_cms > ./$(shell date +"%Y-%m-%d")-streetnoise_cms_DEV.dump

prod-migrate:
	$(DC_PROD) run cms python manage.py migrate
	$(DC_PROD) run cms python manage.py sync_page_translation_fields
	$(DC_PROD) run cms python manage.py update_translation_fields

prod-upgrade:
	$(DC_PROD) build $(DC_BUILD_ARGS)
	$(DC_PROD) pull
	$(DC_PROD) stop cms
	$(MAKE) prod-migrate
	$(DC_PROD) up -d

prod-upgrade-quick:
	$(DC_PROD) pull
	$(DC_PROD) build $(DC_BUILD_ARGS)
	$(DC_PROD) stop cms
	$(DC_PROD) up -d

prod-dump-db:
	$(DC_PROD) exec db pg_dump -U streetnoise_cms streetnoise_cms > ~/$(shell date +"%Y-%m-%d")-streetnoise_cms.dump

prod-update-gigs:
	$(DC_PROD) run cms python manage.py update-gigs-from-gigo

make critical-css:
	node acclaimed.js
