from .common import *

SECRET_KEY = 'xbf)3kqdld3!gu53k9ol@w_tj91hf%9n(4dl7(jo%0xni@a&80'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# email settings 
EMAIL_BACKEND ='django.core.mail.backends.console.EmailBackend'