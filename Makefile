#DC=sudo docker-compose
DC=podman-compose
DC_PROD=$(DC) -f docker-compose.yml
DC_DEV=$(DC) -f docker-compose.dev.yml

dev-db-up:
	podman-compose -f docker-compose.dev.yml up -d

dev-serve:
	python manage.py runserver 8001

dev-reset:
	podman-compose -f docker-compose.dev.yml down
	podman volume rm cms_streetnoise_dev_db
	podman-compose -f docker-compose.dev.yml up -d
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
	$(DC_PROD) build
	$(DC_PROD) pull
	$(DC_PROD) stop cms
	$(MAKE) prod-migrate
	$(DC_PROD) up -d
