import environ
import os
from pathlib import Path

env = environ.Env(
    DEBUG=(bool, False),
)

BASE_DIR = Path(__file__).resolve().parent.parent

environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

SECRET_KEY = env('SECRET_KEY')

DEBUG = bool(env('DEBUG'))

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    # Core
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',

    # 3rd party
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'tinymce',
    'tailwind',
    'django_browser_reload',

    # Local
    'theme',
    'pages.apps.PagesConfig',
    'form_helpers.apps.FormHelpersConfig',
    'custom_user.apps.CustomUserConfig',
    'contact.apps.ContactConfig',
    'jobs.apps.JobsConfig',
    'dashboard.apps.DashboardConfig',
]

# if DEBUG is True:
#     INSTALLED_APPS += ['django_browser_reload', ]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_browser_reload.middleware.BrowserReloadMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

# if DEBUG is True:
#     MIDDLEWARE += ['django_browser_reload.middleware.BrowserReloadMiddleware', ]

ROOT_URLCONF = 'timebank.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'timebank.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE':   'django.db.backends.postgresql',
        'NAME':     env('DB_NAME'),
        'USER':     env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST':     env('DB_HOST'),
        'PORT':     env('DB_PORT'),
    }
}

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static'
STATICFILES_DIRS = [
    BASE_DIR / 'staticfiles',
]

# Media files setup
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Storages setup
STORAGES = {
    'default': {
        'BACKEND': 'django.core.files.storage.FileSystemStorage',
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}

# Email settings
# TODO: expand this for production use
if DEBUG is True:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Tailwind settings

TAILWIND_APP_NAME = 'theme'
NPM_BIN_PATH = env('NPM_BIN_PATH')
INTERNAL_IPS = [
    '127.0.0.1',
]

# Auth settings

SITE_ID = 1
AUTH_USER_MODEL = 'custom_user.CustomUser'
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True
ACCOUNT_FORMS = {
    'login': 'custom_user.forms.CustomAllauthLoginForm',
    'signup': 'custom_user.forms.CustomAllauthSignupForm',
    'set_password': 'custom_user.forms.CustomAllauthSetPasswordForm',
    'reset_password': 'custom_user.forms.CustomAllauthResetPasswordForm',
    'change_password': 'custom_user.forms.CustomAllauthChangePasswordForm',
    'reset_password_from_key': 'custom_user.forms.CustomAllauthResetPasswordKeyForm',
}
ACCOUNT_USER_DISPLAY = 'timebank.helpers.helpers.get_user_full_name'
SOCIALACCOUNT_PROVIDERS = {}
LOGIN_REDIRECT_URL = 'pages:login_success'
ACCOUNT_LOGOUT_REDIRECT_URL = 'pages:home'

TINYMCE_DEFAULT_CONFIG = {
    "height": "450px",
    "menubar": "file edit view insert format tools table help",
    "plugins": "advlist autolink lists link image charmap print preview anchor searchreplace visualblocks code "
    "fullscreen insertdatetime media table paste code help wordcount spellchecker",
    "toolbar": "undo redo | bold italic underline | fontsizeselect formatselect | alignleft "
    "aligncenter alignright alignjustify | outdent indent | numlist bullist | forecolor "
    "backcolor | link anchor codesample | "
    "a11ycheck ltr rtl | showcomments addcomment code",
}
