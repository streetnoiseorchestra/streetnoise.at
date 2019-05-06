DC=sudo docker-compose
DC_PROD=$(DC) -f docker-compose.yml
DC_DEV=$(DC) -f docker-compose.dev.yml

dev-db-up:
	$(DC_DEV) up -d db

dev-serve:
	python manage.py runserver 8001

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
	$(DC_PROD) run --rm cms python manage.py migrate
	$(DC_PROD) run --rm cms python manage.py sync_page_translation_fields
	$(DC_PROD) run --rm cms python manage.py update_translation_fields
