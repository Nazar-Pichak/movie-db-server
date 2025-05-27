from .base import *
from .development import GENRES

GENRES = GENRES + [
    "horror",
    "thriller",
    "mystery",
    "documentary",
    "fantasy",
    "historical",
    "biography",
    "crime",
    "musical",
    "western"
]

ALLOWED_HOSTS = ["nazar2025.pythonanywhere.com"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR.parent / 'development-db.sqlite3',
    }
}


CORS_ALLOW_ALL_ORIGINS = True
CSRF_TRUSTED_ORIGINS = [
    "https://movie-db-client.vercel.app/movies"
]

STATIC_ROOT = os.path.join(BASE_DIR.parent, 'staticfiles')