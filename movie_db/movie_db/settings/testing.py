from .base import *

GENRES = [
    "test-genre-a",
    "test-genre-b"
]

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

# While setting up the test environment, we use a different database
# to avoid conflicts with development data. So it will generate a new
# database file in the directory structure, when we change mode to testing.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR.parent / 'testing-db.sqlite3',
    }
}