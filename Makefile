dev-makemigrations:
	python manage.py makemigrations

dev-migrate: dev-makemigrations
	python manage.py migrate
	python manage.py sync_page_translation_fields
	python manage.py update_translation_fields

dev-serve:
	python manage.py runserver 8001

serve: dev-migrate dev-serve

prod-migrate:
	docker-compose run --rm cms python manage.py migrate
	docker-compose run --rm cms python manage.py sync_page_translation_fields
	docker-compose run --rm cms python manage.py update_translation_fields
