"""
ASGI config for djangoORM project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

import django

from django.core.wsgi import get_wsgi_application
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.wsgi import WSGIMiddleware

from fastapi.staticfiles import StaticFiles

from djangoORM import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoORM.settings')
django.setup()

application = get_wsgi_application()

from fastapi_core import app


fastapiapp = app


# Собираем комплексное приложение (FastAPI + Django WSGI)
def create_application(fastapp):
    fastapp.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.ALLOWED_HOSTS] or ["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    fastapp.mount(f"/django", WSGIMiddleware(application))

    fastapp.mount("/static", StaticFiles(directory="static"), name="static")

    return fastapp


# uvicorn djangoORM.asgi:comp_app --port 8000 --host 0.0.0.0 --reload
comp_app = create_application(fastapiapp)
