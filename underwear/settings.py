import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = "django-insecure-2%se!c56@**$$kgin4tzo7dyxg(7v4$+uj_+t52)nj!5ir$lfv"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []  


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "core",
    'social_django',
    'social.apps.django_app.default', 
]


#AUTHENTICATION_BACKENDS = (
#    'social_core.backends.google.GoogleOAuth2',
#    'django.contrib.auth.backends.ModelBackend',
#)
#
#SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '97525770862-bgtenjjlrohrqj83hr5c2jfptqq9jphe.apps.googleusercontent.com'  # Laisser vide
#SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'  # Laisser vide
#LOGIN_URL = 'login'
#LOGOUT_URL = 'logout'
#LOGIN_REDIRECT_URL = 'index'


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'core.nbr_produits.CartItems',
    'social_django.middleware.SocialAuthExceptionMiddleware',
   
    
    

]

ROOT_URLCONF = "underwear.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, 'templates')],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "social_django.context_processors.backends",
                
                
            ],
        },
    },
]



WSGI_APPLICATION = "underwear.wsgi.application"
#LOGIN_URL = 'login'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}




# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


STATIC_URL = "/static/"

VENV_PATH = os.path.dirname(BASE_DIR)
STATIC_ROOT = os.path.join("static_root")
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media_root")
print(MEDIA_ROOT)
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')

]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

#social app custum settings
AUTHENTICATION_BACKENDS = [
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
    
]

#LOGIN_ERROR_URL = '/login/error/'


LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'http://localhost:8000/social-auth/complete/google-oauth2/'

LOGOUT_URL = 'logout'
#LOGOUT_REDIRECT_URL = 'login'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '478611775698-njve311id87qc4m95747ikmf411p64vi.apps.googleusercontent.com'
SECRET_KEY = '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' 
#SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '######################'
SOCIAL_AUTH_RAISE_EXCEPTIONS = False
