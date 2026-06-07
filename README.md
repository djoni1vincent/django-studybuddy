# Django Course Project

A Django-based web application for managing courses, discussion rooms, and community interactions.

## Course Reference

This project follows the course tutorial:

- **YouTube**: [Django Course - Dennis Ivy](https://www.youtube.com/watch?v=PtQiiknWUcI)

![alt text](https://github.com/user-attachments/assets/01e47ae9-f462-4d22-af96-8db3d64f7560 "website")

## Project Overview

This is a full-stack Django application that demonstrates key concepts including:

- User authentication and management
- Data modeling with Django ORM
- Form handling and validation
- Template rendering with Django templates
- Database migrations
- URL routing

## Project Structure

```
courseprj/
├── manage.py                 # Django management script
├── db.sqlite3               # SQLite database
├── courseprj/               # Main project settings
│   ├── settings.py          # Django settings
│   ├── urls.py              # Project URL configuration
│   ├── asgi.py              # ASGI config
│   └── wsgi.py              # WSGI config
├── base/                    # Main application
│   ├── models.py            # Data models
│   ├── views.py             # View logic
│   ├── forms.py             # Form definitions
│   ├── urls.py              # App URL routes
│   ├── admin.py             # Django admin config
│   ├── migrations/          # Database migrations
│   └── templates/
│       └── base/            # App templates
│           ├── home.html    # Home page
│           ├── room.html    # Room detail view
│           └── room_form.html # Room creation/edit form
└── templates/
    ├── main.html            # Base template
    └── navbar.html          # Navigation component
```

## Features

- **Room Management**: Create, read, update, and delete rooms
- **Discussion Topics**: Organize rooms by topics
- **User Hosting**: Users can host and manage their rooms
- **Message System**: Send and receive messages within rooms
- **Responsive Design**: Mobile-friendly templates

## Installation

1. **Clone the repository**

   ```bash
   cd /Users/djoni1vincent/dev/Django/django-course
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**

   ```bash
   cd courseprj
   python manage.py migrate
   ```

5. **Create a superuser** (for admin access)
   ```bash
   python manage.py createsuperuser
   ```

## Running the Application

```bash
cd courseprj
python manage.py runserver
```

The application will be available at `http://localhost:8000/`

Access the admin panel at `http://localhost:8000/admin/`

## Models

### Topic

- Represents discussion topics for organizing rooms

### Room

- Main model for discussion rooms
- Fields: name, description, topic, host, created, updated

### Message

- User messages within rooms
- Fields: user, room, body, created, updated

## Technologies Used

- **Django**: Web framework
- **Python**: Programming language
- **SQLite**: Database (development)
- **HTML/CSS**: Frontend templates

## Learning Outcomes

By following this project, you'll learn:

- Django MTV (Model-Template-View) architecture
- Django ORM for database operations
- User authentication systems
- Form validation and handling
- Template inheritance and static files
- URL routing and namespacing
- Admin interface customization

## Next Steps

- Extend authentication with email verification
- Add search functionality for rooms
- Implement real-time messaging with WebSockets
- Deploy to production (Heroku, AWS, etc.)

## Resources

- [Django Official Documentation](https://docs.djangoproject.com/)
- [Django Best Practices](https://docs.djangoproject.com/en/stable/topics/)
- [Python Official Documentation](https://www.python.org/doc/)

---

Happy learning! 🎓
