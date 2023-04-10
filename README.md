## O2RUS Django Gas Stations parser

### Requirements:
#### - Python 3.11
#### - [poetry](https://python-poetry.org/docs/)
#### - Docker

### Установка
#### Дисклеймер: окружение, которое создаётся poetry, по-умолчанию python 3.11 версии, поэтому рекомендую при установке poetry указать python 3.11, либо же поставьте окружение вручную на случай, если у вас указана другая версия:
        poetry env use python3.11

#### Для начала укажите в .env.ex SECRET_KEY от Django, создайте базу данных и укажите её в POSTGRE_DSN (URL), затем пропишите:
    ./install.sh

#### Если вы хотите контейнезировать бота:
	./docker_install.sh
#### и введите необходимые данные.
В контейнере в settings.py в ALLOWED_HOSTS укажите IP-адрес контейнера
---
#### Если программа не была контейнезирована, и вы запустили install.sh, как скрипт установит необходимое, пропишите:
    ./start.sh
---
#### Если вы решили остановить контейнер и запустить на хосте, пропишите в главной директории:
```
sed -i 's/db/localhost/1' .env.ex	
./start.sh
```
---
##### API-ключ вызывается по адресу https://127.0.0.1:8000/gas_stations

### Какие инструменты я использовал?
##### - PostgreSQL
##### - Django
##### - DRF
##### - Playwright
##### - Schedule
##### - Pydantic
##### - Flake8
##### - Shell script
