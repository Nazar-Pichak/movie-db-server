from .base import *

GENRES = [
    "sci-fi",
    "adventure",
    "action",
    "romantic",
    "animated",
    "comedy"
]

# Change the BASE_DIR to point to the parent directory, to match the structure of the project

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR.parent / 'development-db.sqlite3',
    }
}


CORS_ALLOW_ALL_ORIGINS = True
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.1:3000",
]