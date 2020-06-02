DOCKER ?= sudo docker
DC ?= sudo docker-compose
DC_ARGS ?=
DC_BUILD_ARGS ?=
DC_PROD ?= $(DC) $(DC_ARGS) -f docker-compose.yml
DC_DEV ?= $(DC) $(DC_ARGS) -f docker-compose.dev.yml

dev-db-up:
	 $(DC_DEV) up -d

dev-serve:
	python manage.py runserver 8001

dev-reset:
	$(DC_DEV) down
	$(DOCKER) volume rm cms_streetnoise_dev_db
	$(DC_DEV) up -d
	sleep 5
	psql -h localhost -U streetnoise_cms streetnoise_cms < streetnoise_cms.dump


serve: dev-migrate dev-serve

dev-makemigrations:
	python manage.py makemigrations

dev-db-load-dump:
	cat ./streetnoise_cms.dump |  sudo docker exec  -i cms_db_1 psql -U streetnoise_cms

dev-migrate: dev-makemigrations
	python manage.py migrate
	python manage.py sync_page_translation_fields
	python manage.py update_translation_fields

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

prod-dump-db:
	$(DC_PROD) exec db pg_dump -U streetnoise_cms streetnoise_cms > ~/$(shell date +"%Y-%m-%d")-streetnoise_cms.dump
