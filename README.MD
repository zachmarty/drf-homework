# Проект курсы и уроки

## Описание пректа

Проект представляет собой сервис для добавления, редактирования, модерации курсов и уроков.

## Подготовка

### Для работы с сервисом необходимо:

- Установить проект
- Установить менеджер зависимостей poetry
- Установить все зависимости командой poetry install
- Активировать виртуальное окружение командой poetry shell
- Создать базу данных в postgresql
- Создать файл переменных окружения .env
- Сохранить в нем слеующие переменные :
SECRET_KEY
DEBUG
NAME (имя базы данных)
USER
PASSWORD
EMAIL_HOST
EMAIL_PORT
EMAIL_HOST_USER
EMAIL_HOST_PASSWORD
EMAIL_USE_SSL
REDIS_URL
- Применить все миграции командой python manage.py migrate
- Запустить сервер командой python manage.py run server

## API

Документация по работе с api представлена по урлу /swagger или /redoc

## Docker

Для запуска docker и docker-compose необходимо использовать команды docker-compose build и docker-compose up. Подключение осуществляется по адресу localhost:8000