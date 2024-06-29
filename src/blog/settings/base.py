import os
from pathlib import Path
import json
import logging

BASE_DIR = Path(__file__).resolve().parent.parent.parent

CONFIG_FILE = '/etc/blog/config.json'

ADMIN_WHITELIST = ['127.0.0.1']


with open(CONFIG_FILE) as f:
    config = json.load(f)
    
    SECRET_KEY = config['SECRET_KEY']


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(message)s',
            },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/tmp/django_errors.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

# Custom logger
logger = logging.getLogger('django')
logger.error("WORKING")

INSTALLED_APPS = [

    # Django Apps
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    ## Admin
    'django.contrib.admin',

    ### OTP
    'django_otp',
    'django_otp.plugins.otp_totp',

    # Misc
    'compressor',
    'sass_processor',
    'django_ckeditor_5', # Rich text editor
    'hitcount',

     # Apps
    'core',
    'user',
    'articles',
    'about',
]


AUTH_USER_MODEL = 'user.User'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_otp.middleware.OTPMiddleware', # OTP

    # Custom
    'core.middleware.admin_restrict.AdminRestrictMiddleware'
]

ROOT_URLCONF = 'blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
            ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [

                # Default
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # Custom
                'core.context_processors.user_info', # FIX: Not in use
                'core.context_processors.nav_items',
                'core.context_processors.socialmedia_icons',
            ],
        },
    },
]

WSGI_APPLICATION = 'blog.wsgi.application'


with open(CONFIG_FILE) as f:
    config = json.load(f)

    DATABASES = {
        'default': {
            'ENGINE': config['databases']['blog']['engine'],
            'NAME': config['databases']['blog']['name'],
            'USER': config['databases']['blog']['user'],
            'PASSWORD': config['databases']['blog']['password'],
            'HOST': config['databases']['blog']['host'],
            'PORT': config['databases']['blog']['port']
        }
    }


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


STATICFILES_FINDERS = ( 
                       'django.contrib.staticfiles.finders.FileSystemFinder',  
                       'django.contrib.staticfiles.finders.AppDirectoriesFinder',    
                       'compressor.finders.CompressorFinder',
                       ) 


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = '/var/www/alexandereriksson.se/static'


MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

COMPRESS_PRECOMPILERS = (    
                         ('text/x-scss', 'django_libsass.SassCompiler'),
                         )

COMPRESS_ENABLED = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

customColorPalette = [
        {
            'color': 'hsl(4, 90%, 58%)',
            'label': 'Red'
            },
        {
            'color': 'hsl(340, 82%, 52%)',
            'label': 'Pink'
            },
        {
            'color': 'hsl(291, 64%, 42%)',
            'label': 'Purple'
            },
        {
            'color': 'hsl(262, 52%, 47%)',
            'label': 'Deep Purple'
            },
        {
            'color': 'hsl(231, 48%, 48%)',
            'label': 'Indigo'
            },
        {
            'color': 'hsl(207, 90%, 54%)',
            'label': 'Blue'
            },
        ]

CKEDITOR_5_CONFIGS = {
'default': {
    'toolbar': ['heading', '|', 'bold', 'italic', 'link', 'bulletedList', 'numberedList', 'blockQuote', 'imageUpload', ],
    },
'comment': {
    'toolbar': ['heading', '|', 'bold', 'italic', 'link', 'bulletedList', 'numberedList', 'blockQuote', ],
    },
'extends': {
    'blockToolbar': [
        'paragraph', 'heading1', 'heading2', 'heading3',
        '|',
        'bulletedList', 'numberedList',
        '|',
        'blockQuote',
        ],
    'toolbar': ['heading', '|', 'outdent', 'indent', '|', 'bold', 'italic', 'link', 'underline', 'strikethrough',
                'code','subscript', 'superscript', 'highlight', '|', 'codeBlock', 'sourceEditing', 'insertImage',
                'bulletedList', 'numberedList', 'todoList', '|',  'blockQuote', 'imageUpload', '|',
                'fontSize', 'fontFamily', 'fontColor', 'fontBackgroundColor', 'mediaEmbed', 'removeFormat',
                'insertTable',],
    'image': {
        'toolbar': ['imageTextAlternative', '|', 'imageStyle:alignLeft',
                    'imageStyle:alignRight', 'imageStyle:alignCenter', 'imageStyle:side',  '|'],
        'styles': [
            'full',
            'side',
            'alignLeft',
            'alignRight',
            'alignCenter',
            ]

        },
    'table': {
        'contentToolbar': [ 'tableColumn', 'tableRow', 'mergeTableCells',
                           'tableProperties', 'tableCellProperties' ],
        'tableProperties': {
            'borderColors': customColorPalette,
            'backgroundColors': customColorPalette
            },
        'tableCellProperties': {
            'borderColors': customColorPalette,
            'backgroundColors': customColorPalette
            }
        },
    'heading' : {
        'options': [
            { 'model': 'paragraph', 'title': 'Paragraph', 'class': 'ck-heading_paragraph' },
            { 'model': 'heading1', 'view': 'h1', 'title': 'Heading 1', 'class': 'ck-heading_heading1' },
            { 'model': 'heading2', 'view': 'h2', 'title': 'Heading 2', 'class': 'ck-heading_heading2' },
            { 'model': 'heading3', 'view': 'h3', 'title': 'Heading 3', 'class': 'ck-heading_heading3' }
            ]
        }
    },
'list': {
    'properties': {
        'styles': 'true',
        'startIndex': 'true',
        'reversed': 'true',
        }
    }
}


