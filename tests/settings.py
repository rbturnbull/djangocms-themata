import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'akfjnakfcjaldunfkhaldfhalshf'
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    
    "cms",    
    'menus',
    'treebeard',
    "cms_bootstrap",    
    "djangocms_themata",
    "tests",
]
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            "context_processors": [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # Required for admin
                'django.contrib.auth.context_processors.auth',  # Required
                'django.contrib.messages.context_processors.messages',  # Required
            ],
        },
    },
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # Required
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Required
    'django.contrib.messages.middleware.MessageMiddleware',  # Required
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

SITE_ID = 1
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
# ROOT_URLCONF = "tests.urls"

USE_TZ = False  # Change to True if you want timezone support

CMSPLUGIN_CASCADE_PLUGINS = []

CMS_CONFIRM_VERSION4 = True