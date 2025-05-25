#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from pathlib import Path
from dotenv import load_dotenv


def main():
    """Run administrative tasks in different environments.
    - base.py contains common settings.
    - development.py contains settings for development.
    - testing.py contains settings for testing.
    - stage.py contains settings for staging.
    - production.py contains settings for production.
    
    Usage:
    Switch environments by setting DJANGO_ENV to 'development', 'testing', 'stage', or 'production'.
    - $env:DJANGO_ENV = "testing" -> For PowerShell (Windows)
    - $env:DJANGO_ENV -> check current environment variable
    """
    BASE_DIR = Path(__file__).resolve().parent
    env = os.getenv("DJANGO_ENV", "development")
    load_dotenv(BASE_DIR / f".env.{env}", override=True)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"movie_db.settings.{env}")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
