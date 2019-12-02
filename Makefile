iniciar:
	@pipenv install

ejecutar:
	@pipenv run python manage.py runserver

ejecutar_worker:
	@pipenv run python manage.py rqworker

crear_migraciones:
	@pipenv run python manage.py makemigrations

migrar:
	@pipenv run python manage.py migrate --noinput

test:
	@echo "${G}Ejecutando tests ...${N}"
ifeq ($(filtro),)
	pipenv run pytest
else
	pipenv run pytest -k $(filtro)
endif

test_live:
ifeq ($(filtro),)
	pipenv run ptw
else
	pipenv run ptw -- -k $(filtro)
endif

reset:
	dropdb --if-exists tca -e; createdb tca
	pipenv run python manage.py migrate --noinput

build_requirements:
	@pipenv lock -r > requirements.txt
	cat requirements.txt

collectstatic:
	pipenv run python manage.py collectstatic

deploy:
	sudo git push heroku master

migrar_en_prod:
	sudo heroku run python manage.py  migrate --noinput
