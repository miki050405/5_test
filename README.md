REST API для простого блога
## Установка

1. Склонируйте репозиторий

```bash
git clone <ссылка_на_репозиторий>
cd 5_TEST
```

2. Создать виртуальное окружение

```bash
python -m venv venv
```

3. Активировать виртуальное окружение

Windows:

```bash
venv\Scripts\activate
```

4. Установить зависимости

```bash
pip install -r requirements.txt
```

5. Создать файл .env

```env
DB_NAME=blog
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432

SECRET=your_secret_key
DEBUG=on
```

6. Применить миграции

```bash
python manage.py migrate
```

7. Создать суперпользователя

```bash
python manage.py createsuperuser
```

8. Запустить сервер

```bash
python manage.py runserver
```

## Документация

Swagger:

```text
http://127.0.0.1:8000/swagger/
```

## Аутентификация

Используется Token Authentication.

Получить токен:

```text
POST /api/v1/users/authorization/
```

Для защищённых запросов необходимо передавать заголовок:

```text
Authorization: Token <your_token>
```
