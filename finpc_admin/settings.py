"""
Django settings for finpc_admin project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path
import pymysql

pymysql.install_as_MySQLdb()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-5k_cs(1x@!^(d1ipo((6j+iq*hy4ndhlqsfcq5u)h81+ef0oe1"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition
AUTH_USER_MODEL = "app.User"

INSTALLED_APPS = [
    "baton",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "app",
    "baton.autodiscover",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "finpc_admin.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "finpc_admin.wsgi.application"

BATON = {
    "SITE_HEADER": "FINPC Admin",
    "SITE_TITLE": "Hello FINPC",
    "INDEX_TITLE": "Site administration",
    "COPYRIGHT": "copyright © 2023 TAEHUN LEE",  # noqa
    "CONFIRM_UNSAVED_CHANGES": True,
    "SHOW_MULTIPART_UPLOADING": True,
    "ENABLE_IMAGES_PREVIEW": True,
    "CHANGELIST_FILTERS_IN_MODAL": True,
    "CHANGELIST_FILTERS_ALWAYS_OPEN": False,
    "CHANGELIST_FILTERS_FORM": True,
    "MENU_ALWAYS_COLLAPSED": False,
    "MENU_TITLE": "메뉴",
    "MESSAGES_TOASTS": True,
    "GRAVATAR_DEFAULT_IMG": "retro",
    "GRAVATAR_ENABLED": True,
    "LOGIN_SPLASH": "/static/core/img/login-splash.png",
    "SEARCH_FIELD": {
        "label": "검색하기...",
        "url": "/search/",
    },
    "MENU": (
        {"type": "title", "label": "main", "apps": ("auth",)},
        {
            "type": "app",
            "name": "auth",
            "label": "Authentication",
            "icon": "fa fa-lock",
            "models": (
                {"name": "user", "label": "Users"},
                {"name": "group", "label": "Groups"},
            ),
        },
        {"type": "title", "label": "Contents", "apps": ("flatpages",)},
        {"type": "model", "label": "Pages", "name": "flatpage", "app": "flatpages"},
        {
            "type": "free",
            "label": "글로벌핀테크산업진흥센터",
            "url": "http://finpc.org/",
            "perms": ("flatpages.add_flatpage", "auth.change_user"),
        },
        {
            "type": "free",
            "label": "고객의 소리",
            "default_open": True,
            "children": [
                {"type": "model", "label": "게시판", "name": "board", "app": "app"},
                {"type": "free", "label": "Another custom link", "url": "http://www.google.it"},
            ],
        },
    ),
}

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "NAME": "finpc_db_1",
        "ENGINE": "django.db.backends.mysql",
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PW"),  # 계정 비밀번호
        "HOST": os.getenv("DB_URL"),  # 데이테베이스 주소(IP)
        "PORT": 3306,  # 데이터베이스 포트(보통은 3306)
        "OPTIONS": {
            "autocommit": True,
            "charset": "utf8mb4",
        },
    },
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "ko-kr"

TIME_ZONE = "Asia/Seoul"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"