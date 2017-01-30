# django_login_logut_auth
Login, logout, password reset/change and authorization in Django 1.10.5 using builtin django.contrib.auth views and forms.

Only required django application is django-bootstrap3, so please install it in your environment first.

Then in settings.py add these :

INSTALLED_APPS = [
    ....
    'bootstrap3',
    'useraccounts',

    ....
]

TEMPLATES = [
    {
        ....
        'DIRS': [
            BASE_DIR + '/STATIK/templates/',
        ]
        .....
    }
]


LOGIN_REDIRECT_URL ='/useraccounts/profile/'
LOGIN_URL ='/useraccounts/ulogin/'

STATIC_ROOT = BASE_DIR + '/STATIK/static/'
STATIC_URL  = '/static/'

Then after doing necessary settings requirements, do the classif stuff :
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
