DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'gams_db',
        'USER': 'root',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
    'games',
]
AUTH_USER_MODEL = 'users.CustomUser'
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'