"""
settings for development
"""
from .base import *

ALLOWED_HOSTS = ["127.0.0.1"]


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
