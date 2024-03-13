import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = str(os.getenv('SECRET_KEY', 'django-insecure-rrf=&q@@)@4t!4%fv_9%cz9^x+*+*kvcf2u8p2(e20zngjrok^'))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', 'False').lower() in ('true', '1', 't')

#ALLOWED_HOSTS = []
ALLOWED_HOSTS = [str(os.getenv('ALLOWED_HOSTS', '*'))]



# Application definition

INSTALLED_APPS = [
    'licenses',
    'dashboard',
    'wagtail_2fa',
    'django_otp',
    'django_otp.plugins.otp_totp',
    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail',
    #'wagtailgeowidget',
    'wagtail_modeladmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'modelcluster',
    'taggit',
    'axes',
    #'django_cleanup.apps.CleanupConfig',
]


AUTHENTICATION_BACKENDS = [
    # AxesStandaloneBackend should be the first backend in the AUTHENTICATION_BACKENDS list.
    'axes.backends.AxesStandaloneBackend',

    # Django ModelBackend is the default authentication backend.
    'django.contrib.auth.backends.ModelBackend',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'wagtail_2fa.middleware.VerifyUserMiddleware',
    #'wagtail_2fa.middleware.VerifyUserPermissionsMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


MIDDLEWARE += ('wagtail.contrib.redirects.middleware.RedirectMiddleware',)
MIDDLEWARE += ('crum.CurrentRequestUserMiddleware',)
MIDDLEWARE += ('axes.middleware.AxesMiddleware',)
#MIDDLEWARE += ('wagtail_2fa.middleware.VerifyUserMiddleware',)
#MIDDLEWARE += ('wagtail_2fa.middleware.VerifyUserPermissionsMiddleware',)


ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
'''

DATABASES = {
    'default': {
        'ENGINE': str(os.getenv('DB_ENGINE', 'django.db.backends.sqlite3')),
        'NAME': str(os.getenv('DB_NAME', 'db.sqlite3')),
        'USER': str(os.getenv('DB_USER')),
        'PASSWORD': str(os.getenv('DB_PASSWORD')),
        'HOST': str(os.getenv('DB_HOST')),
        'PORT': str(os.getenv('DB_PORT')),
    },
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'id-id'

TIME_ZONE = 'Asia/Jakarta'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Custom User Model
#AUTH_USER_MODEL = 'accounts.User'

# Custom User Model - Wagtail Integration
#WAGTAIL_USER_EDIT_FORM = 'accounts.forms.CustomUserEditForm'
#WAGTAIL_USER_CREATION_FORM = 'accounts.forms.CustomUserCreationForm'
#WAGTAIL_USER_CUSTOM_FIELDS = ['organization']

# Wagtail
WAGTAIL_SITE_NAME = str(os.getenv('WAGTAIL_SITE_NAME', 'BackOne License'))
WAGTAILADMIN_BASE_URL = str(os.getenv('WAGTAILADMIN_BASE_URL', 'http://localhost:8000'))
WAGTAIL_ENABLE_WHATS_NEW_BANNER = False
WAGTAIL_ENABLE_UPDATE_CHECK = False


# AXES
AXES_COOLOFF_TIME = float(os.getenv('AXES_COOLOFF_TIME', 2))
AXES_RESET_ON_SUCCESS = True
AXES_LOCKOUT_PARAMETERS = ['username']
AXES_LOCKOUT_TEMPLATE = 'axes/block.html'
AXES_IPWARE_PROXY_COUNT = int(os.getenv('AXES_IPWARE_PROXY_COUNT', 0))


# GOOGLE_MAPS
#GOOGLE_MAPS_V3_APIKEY = str(os.getenv('GOOGLE_MAPS_V3_APIKEY'))
#MAP_CENTER = str(os.getenv('MAP_CENTER', "{lat: -1.233982000061532, lng: 116.83728437200422}"))
#MAP_ZOOM = int(os.getenv('MAP_ZOOM', 5))

# MAP DASHBOARD - IN SECONDS
#MAP_REFRESH_INTERVAL = int(os.getenv('MAP_REFRESH_INTERVAL', 300))

# GEO Widget
#GEO_WIDGET_DEFAULT_LOCATION = {'lat': -6.175349682264274, 'lng': 106.82715256580741}
#GEO_WIDGET_ZOOM = int(os.getenv('GEO_WIDGET_ZOOM', '15'))

# CSRF
CSRF_TRUSTED_ORIGINS = [WAGTAILADMIN_BASE_URL]

# RSA KEY BIT
# At least 2048 bit
RSA_KEY_BIT = int(os.getenv('RSA_KEY_BIT', 2048))

# 2FA
WAGTAIL_2FA_REQUIRED = os.getenv('WAGTAIL_2FA_REQUIRED', 'False').lower() in ('true', '1', 't')

# DJANGO SESSION
SESSION_COOKIE_AGE = int(os.getenv('SESSION_COOKIE_AGE', 3600))

