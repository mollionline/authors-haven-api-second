from .base import *

from .base import env

DEBUG = True


SECRET_KEY = env('DJANGO_SECRET_KEY', default='django-insecure-148hvrs@idp!n2aru6o%wv9lqohehp6o2$6jv$ah#xf0&ih1)r')


ALLOWED_HOSTS = ['localhost', '0.0.0.0', '127.0.0.1']