import os
import django_heroku

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%hxpxexn^^@^nhmshmxn#*2le7$cya%s!81vc54m2=2@zx06$n'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['vh-cam-yde.herokuapp.com', 'www']


# Application definition

INSTALLED_APPS = [

    #==================App accounts
    'accounts.apps.AccountsConfig',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary_storage',
    'cloudinary',

    #==========my library
    'widget_tweaks',

    #==================App remplissage
    'remplissages.apps.RemplissagesConfig',

    #==================App rapport
    'rapport.apps.RapportConfig',

    #==================App suivie
    'suivie.apps.SuivieConfig',

    #==================App gallerie
    'gallerie.apps.GallerieConfig',

    #==================App gallerie
    'temoignage.apps.TemoignageConfig',

    #==================App history
    'history.apps.HistoryConfig'
]


SHORT_DATE_FORMAT = 'd/m/Y'

DATE_INPUT_FORMATS = [
    '%d/%m/%Y'
]

TIME_INPUT_FORMATS = [
    '%H:%M',        # '14:30'
]

LOGIN_URL = 'accounts:user_login'
#LOGIN_REDIRECT_URL = '/accounts/profile/'
#LOGOUT_REDIRECT_URL = None

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
     'whitenoise.middleware.WhiteNoiseMiddleware', # White Noise
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'vhproject2021.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'vhproject2021.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd41vuilp6shr4s',
        'USER': 'ieiosgipeemlvw',
        'PASSWORD': '95ccf50b9f8d35194f8b67d979aa16b3cbd95f017d0806c2296cca4c3449256a',
        'HOST': 'ec2-52-209-171-51.eu-west-1.compute.amazonaws.com',
        'POST': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'fr-fr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
django_heroku.settings(locals())
#STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'vh-cam',
    'API_KEY': '259285251143441',
    'API_SECRET': 'aJvmF3SsffpBJFzVUcF8Bi6JPuM'
}

#MEDIA_URL = '/media/'
#MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
DEFAULT_FILE_STORAGE='cloudinary_storage.storage.MediaCloudinaryStorage'
