# yourcadastre

Cервис, который принимает запрос с указанием кадастрового номера, широты и долготы, эмулирует отправку запроса на внешний сервер, который может обрабатывать запрос до 60 секунд. Затем должен отдавать результат запроса. Считается, что внешний сервер может ответить `true` или `false`.

### Технологии:
- Django DRF
- PostgreSQL
- drf-yasg
- celery
- redis

## Подготовка и запуск проекта:

```sh
git clone git@github.com:AlexBesedin/yourcadastre.git
```
Создайте файл содержащий переменные виртуального окружения (.env) и добавьте секретный ключ джанго
```sh
cd yourcadastre/main
touch .env
```
```sh
SECRET_KEY=<Секретный ключ>
POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
```
Разверните контейнеры и выполните миграции:
```sh
cd gyourcadastre/infra/
sudo docker-compose up -d --build
sudo docker-compose exec backend python manage.py migrate
```

### Документация:
```sh
http://ваш_ip_адрес/api/docs/
```

АВТОР: 

[Беседин Алексей](https://github.com/AlexBesedin)

TG: @beszedin