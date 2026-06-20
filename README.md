REST API для простого блога

## Установка
1. Склонируйте репозиторий
```bash
git clone https://github.com/miki050405/5_test
cd 5_test
```

2. Создайте виртуальное окружение
```bash
python -m venv venv
```

3. Активируйте виртуальное окружение
```bash
#Windows:
venv\Scripts\activate
# macOS / Linux:
source venv/bin/activate
```

4. Установите зависимости
```bash
pip install -r requirements.txt
```

5. Создайте файл .env для хранения параметров бд, секретного ключа и DEBUG
```env
DB_NAME=название бд
DB_USER=имя пользователя бд
DB_PASSWORD=пароль
DB_HOST=хост
DB_PORT=порт (обычно 5432)

SECRET=ваш секретный ключ

DEBUG=состояние DEBUG (on если True, off если False)
```

6. Примените миграции
```bash
python manage.py migrate
```

7. Создайте суперпользователя
```bash
python manage.py createsuperuser
```

8. Запустите сервер
```bash
python manage.py runserver
```

## Документация
Swagger:
```text
http://127.0.0.1:8000/swagger/
```
