# Editorial Andina App

## Requisitos

- Python 3.x
- Django
- Requests (para el frontend)

## Instalación

```bash
pip install django requests
```

## Backend

```bash
cd backend
python manage.py makemigrations api
python manage.py migrate
python manage.py runserver
```

## Frontend

```bash
cd frontend
python app.py
```

## Características

- Gestión de autores y libros.
- Respaldo automático cada 60 segundos.
