# StudyBuddy Project

A Django-based web application for managing courses, discussion rooms, and community interactions.

## Course Reference

This project follows the course tutorial:

- **YouTube**: [Django Course - Dennis Ivy](https://www.youtube.com/watch?v=PtQiiknWUcI)

![alt text](https://github.com/user-attachments/assets/43495acb-89fb-490f-bdd4-972249de28e1)

## Project Overview

This is a full-stack Django application that demonstrates key concepts including:

- User authentication and management
- Data modeling with Django ORM
- Form handling and validation
- Template rendering with Django templates
- Database migrations
- URL routing

## Features

- User registration, authentication, and profile management
- Create, edit, and delete rooms
- Comments inside rooms (create, edit, delete)
- Search rooms by name, topic, and description
- Topic categories for rooms with room count
- Dedicated topics browsing page (`/topics/`)
- Recent activity feed (`/activities/`)
- User profiles with avatar upload and bio
- Responsive layout with mobile-friendly navigation

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

- `base/` — main app (models, views, templates, forms)
- `courseprj/` — project config (settings, urls)
- `templates/` — shared base templates (main.html, navbar)
- `static/` — static files (styles, scripts, images)

## URL Reference

| URL | Name | Description |
|-----|------|-------------|
| `/` | `home` | Main page with rooms, topics, and activity |
| `/topics/` | `topics` | Browse all topics |
| `/activities/` | `activities` | Recent activity feed |
| `/login/` | `login` | Login page |
| `/register/` | `register` | Registration page |
| `/logout/` | `logout` | Logout |
| `/profile/<username>/` | `user-profile` | User profile page |
| `/room/<pk>/` | `room` | Room detail with comments |
| `/create-room/` | `create-room` | Create a new room |
| `/update-room/<pk>/` | `update-room` | Edit a room |
| `/delete-room/<pk>/` | `delete-room` | Delete a room |
| `/update-user/` | `update-user` | Edit user profile |
| `/delete-comment/<pk>/` | `delete-comment` | Delete a comment |
| `/edit-comment/<pk>/` | `edit-comment` | Edit a comment |


## Learning Outcomes

By following this project, you'll learn:

- Django MTV (Model-Template-View) architecture
- Django ORM for database operations
- User authentication systems
- Form validation and handling
- Template inheritance and static files
- URL routing and namespacing
- Admin interface customization


## Resources

- [Django Official Documentation](https://docs.djangoproject.com/)
- [Django Best Practices](https://docs.djangoproject.com/en/stable/topics/)
- [Python Official Documentation](https://www.python.org/doc/)
