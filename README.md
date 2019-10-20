# pd-diplom-webshop

Бояршин Д.И.

Дипломная работа к профессии Python-разработчик (API Сервис заказа товаров для розничных сетей)

## Установка

Склонируйте репозиторий с помощью git

    git clone https://github.com/DBoyara/pd-diplom.git

Перейти в папку:
```bash
cd pd-diplom
```
Создать и активировать виртуальное окружение Python.

Установить зависимости из файла **requirements.txt**:
```bash
pip install -r requirements.txt
```
Перейти в папку с manage.py:
```bash
cd orders
```
# Выполнить следующие команды:

* Команда для создания миграций приложения для базы данных
```bash
python manage.py makemigrations
python manage.py migrate
```

* Команда для запуска приложения
```bash
python manage.py runserver
```
* Приложение будет доступно по адресу: `http://127.0.0.1:8000/`

API также опубликовано на сервере POSTMAN:

    https://documenter.getpostman.com/view/8643249/SVtbQ5aJ
