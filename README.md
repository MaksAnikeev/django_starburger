# Сайт доставки еды Star Burger

Это сайт сети ресторанов Star Burger. Здесь можно заказать превосходные бургеры с доставкой на дом.

![скриншот сайта](https://dvmn.org/filer/canonical/1594651635/686/)


Данный репозиторий является копией репозитория с сайтом [бургеров](https://github.com/MaksAnikeev/star-burger).
Данный репозиторий создан для демонстрации деплоя проекта Джанго в докере с использованием
`docker-compose`, `gunicorn`, `nginx`, `postgree`

### Запуск через Докер
Скачайте код:
```
git clone https://github.com/MaksAnikeev/django_starburger.git
```

Перейдите в каталог проекта:
```
cd star-burger
```
Откройте файл `docker-compose.yml` и заполните переменные окружения

Для вычисления расстояний между клиентом и различными ресторанами потребуется
`YANDEX_API_KEY`. Его можно получить на сайте [яндекс разработчика](https://developer.tech.yandex.ru/services/), а это
[инструкция по получению ключа](https://dvmn.org/encyclopedia/api-docs/yandex-geocoder-api/). Полученный ключ необходимо записать в .env
```
YANDEX_API_KEY=ваш ключ
```
Если вы запускаете проект не на локальном компьютере, а на арендованном сервере,
то необходимо прописать ip сервера
```
ALLOWED_HOSTS=80.249....
```
Для просмотра и фиксации ошибок при работе сайта - необходимо зарегестрироваться на сайте [rollbar](https://rollbar.com/)
Создать проект и записать project_access_token. Вы можете этого не делать,
если вам не нужно получать информацию об ошибках в роллбаре.
Тогда укажите `ROLLBAR=False`. Если же нужны записи ошибок, то необходимо
прописать `ROLLBAR=True` и указать следующие 3 переменные окружения:
```
ROLLBAR_ACCESS_TOKEN='521c.....'
```
В зависимости от того запустили вы сервер в "боевом" режиме или в режиме
"отладки" необходимо указать
```
DEV=True - для отладки
DEV=False - для боевого
```
и ваше имя
```
USER='max'
```

Создайте базу данных в [PostgreSQL](https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04)
и получите данные `USER`, `PASSWORD`, имя базы данных `NAME` и внесите эти данные
в виде URL
```
POSTGRES_URL='postgres://[user[:password]@][netloc][:port][/dbname][?param1=value1&...]'
пример
POSTGRES_URL='postgres://max:12345@localhost/maxburger1'
```

так должен выглядеть полностью заполненный файл с переменными:
```
environment:
      SECRET_KEY: 'replace_me'
      DJANGO_SUPERUSER_USERNAME: admin
      DJANGO_SUPERUSER_PASSWORD: admin
      DJANGO_SUPERUSER_EMAIL: admin@example.com
      YANDEX_API_KEY: 485691e3-.....
      ALLOWED_HOSTS: 80.249.....,127.0.0.1:8080,127.0.0.1,localhost,starburger
      DEBUG: 'False'
      ROLLBAR: 'False'
      DEV: 'False'
      USER: 'max'
      ROLLBAR_ACCESS_TOKEN: 521c8a98a37348669908...........
      POSTGRES_URL: postgres://max:Anykey@pgdb:5432/maxburger
```
А потом запустите `docker-compose.yml` в каталоге где он находится:
```
docker-compose up
```
Данный скрипт создаст 3 докер контейнера `backend`, `pgdb`, `nginx`, установит в них
все зависимости из requirements.txt и необходимые библиотеки JS, соберет фронтенд,
соберет всю статику в одну папку, сделает миграции и запустит сайт.
Сайт будет доступен на локале http://127.0.0.1/ или на вашем сервере

### Установка базы данных с картинками и заказами
Определите ид запущенных контейнеров:
```
docker ps -a
```
Запустите командную строку в этом контейнере:
```
docker exec -it b5d116ad83cc bash
```
Сделайте доступным для выполнения файл `manage.py`
```
root@4bf038e7a9d6:/app# chmod +x manage.py
```
Залейте базу данных с джейсон файла `starburger.json`:
```
root@4bf038e7a9d6:/app#  ./manage.py loaddata starburger.json
```

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
