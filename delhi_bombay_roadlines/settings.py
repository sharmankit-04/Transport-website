from pathlib import Path
import os
from django.contrib.messages import constants as messages

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

ROOT_URLCONF = 'delhi_bombay_roadlines.urls'

# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ji)#20y8v3v2a_g0%1%x^cucuf6oxcwd%$e$$n)g1w8yt!+(ax'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  # Set this to False in production

ALLOWED_HOSTS = ['localhost', '127.0.0.1']  # Allow local access

# Installed apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'transport',  # Your custom app
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
LOGIN_URL = '/accounts/login/'
# Template settings
# settings.py
import os  # at the top

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # required for admin sidebar
                'django.contrib.auth.context_processors.auth',  # required for admin auth
                'django.contrib.messages.context_processors.messages',  # required for admin messages
            ],
        },
    },
]

# Static files
STATIC_URL = 'static/'

# PostgreSQL Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dbr',
        'USER': 'ankit',
        'PASSWORD': 'ankit',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


