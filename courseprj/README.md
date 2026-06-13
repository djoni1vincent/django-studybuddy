# courseprj

A Django learning project — a simple discussion room (forum) application.

Built while following the [Django 7 Hour Course (Dennis Ivy)](https://www.youtube.com/watch?v=PtQiiknWUcI) and Django's official documentation.

## Features

- User registration and authentication
- Create, edit, and delete rooms
- Comments inside rooms
- Search rooms by name, topic, and description
- Topic categories for rooms

## Stack

- Python 3.13
- Django 6.0
- SQLite
- uv

## Setup

```bash
uv sync
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000/

## Project Structure

- `base/` — main app (models, views, templates)
- `courseprj/` — project config (settings, urls)
- `templates/` — shared base templates (main.html, navbar)
