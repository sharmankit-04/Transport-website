# delhi_bombay_roadlines/wsgi.py

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'delhi_bombay_roadlines.settings')

application = get_wsgi_application()

# """
# WSGI config for delhi_bombay_roadlines project.

# It exposes the WSGI callable as a module-level variable named ``application``.

# For more information on this file, see
# https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
# """

# import os

# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'delhi_bombay_roadlines.settings')

# application = get_wsgi_application()
