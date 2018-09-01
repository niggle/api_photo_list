from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'q0(d%5-0p%&mq6^x+9@i7iox9e4vup56!rv282p0y%=m_&0_iq'

ALLOWED_HOSTS = ['*']