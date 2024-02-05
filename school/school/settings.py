"""
Django settings for school project.

Generated by 'django-admin startproject' using Django 4.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-8lqh@p%@zq9g^74+z9fin+ku1tld+r*1wq@o-pufw&=edym^ns'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['https://school-ms.onrender.com/']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'school_admin',
    'student',
    'teacher',
    'common',
    'student_api',
    'rest_framework',
    'google_api',
    'student_fend',
    "corsheaders",
    'blog'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
]

CORS_ALLOW_ALL_ORIGINS=True

ROOT_URLCONF = 'school.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR/'school_admin/templates/school_admin',
            BASE_DIR/'student/templates/student',
            BASE_DIR/'teacher/templates/teacher',
            BASE_DIR/'common/templates/common'
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'school.wsgi.application'

AUTH_USER_MODEL = 'blog.User'
LOGIN_REDIRECT_URL = 'blog:blog_list'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME':'schooldb',
#         'USER':'postgres',
#         'PASSWORD':'iTr114718S5RBDGVyg5dL9dRQAh6oAzW',
#         # 'HOST':'host.docker.internal',
#         # 'HOST': '172.17.0.2',
#         # 'HOST': 'dpg-cn0859v109ks73ben9qg-a.oregon-postgres.render.comlocalhost',
#         'HOST': 'dpg-cn0859v109ks73ben9qg-a.oregon-postgres.render.com',

#         'PORT':'5432',
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'schooldb_qqrx',  # Name of your PostgreSQL database
        'USER': 'schooldb_qqrx_user',  # PostgreSQL user
        'PASSWORD': 'iTr114718S5RBDGVyg5dL9dRQAh6oAzW',  # Password for the PostgreSQL user
        'HOST': 'dpg-cn0859v109ks73ben9qg-a.oregon-postgres.render.com',  # Hostname of the PostgreSQL database server
        'PORT': '5432',  # Port number for the PostgreSQL database server
    }
}



# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')

STATICFILES_DIRS=[
    os.path.join(BASE_DIR,'school_admin/static'),
    os.path.join(BASE_DIR,'student/static'),
    os.path.join(BASE_DIR,'teacher/static'),
    os.path.join(BASE_DIR,'common/static'),
]
# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'aastroaurora@gmail.com'
EMAIL_HOST_PASSWORD = 'scwcxkyhwkxtiext'

# LOGGING ={
#     'version': 1,
#     'disable existing loggers':False,
#     'handlers':{
#         'file':{
#             'level': DEBUG,
#             'class':'logging.FileHandler',
#             'filename':BASE_DIR/'logs/debug.log',
           
#         },

#         'console':{
#             'class':'logging.StreamHandler',
#         },
        
#         'infofle':{
#             'level':'INFO',
#             'class':'logging.FileHandler',
#             'filename': BASE_DIR/'logs/info.log',
#             'formatter': 'simpleRe',
#         },

#     },
#     'loggers':{
#         'django':{
#             'handlers': ['file','console','infofile'],
#             'level': DEBUG,
#             # 'propogate':True,
#             # 'level': os.getenv('DJANGo_LOG_LEVEL','DEBUG')
#         },
#     },
#     'formatters':{
#         'simpleRe': {
#             'formate': '{level} {asctime} {module} {message}',
#             'style':'{',

            

#         }
#     }

# }
