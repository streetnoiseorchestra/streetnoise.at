makemigrations:
	python manage.py makemigrations

migrate:
	python manage.py makemigrations
	python manage.py migrate 
	python manage.py sync_page_translation_fields
	python manage.py update_translation_fields

serve: 
	python manage.py runserver 8001
