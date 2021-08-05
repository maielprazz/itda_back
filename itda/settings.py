from pathlib import Path
import os
from dotenv import load_dotenv
import datetime
import ldap
from django_auth_ldap.config import LDAPSearch, GroupOfNamesType


load_dotenv()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-i=p77-)mhwdjafcq^!%h%-*vp144@ljxbrw6970y8p6g1j83d9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
CORS_ORIGIN_ALLOW_ALL = True
ALLOWED_HOSTS = ['jkthomaasql03','localhost','*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'drf_yasg',
    'rest_framework',
    # 'base',
    'authentication',
    # 'users',
    'expenses',
    'mod_wsgi.server',
]

SWAGGER_SETTINGS={
    'SECURITY_DEFINITIONS':{
        'Bearer' : {
            'type' : 'apiKey',
            'name' : 'Authorization',
            'in' : 'header'
        }
    }
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'itda.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'frontend/build'),
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

WSGI_APPLICATION = 'itda.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'old': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    'default': {
            'ENGINE': 'mssql',
            'NAME': 'DJANGO',
            'USER': 'django',
            'PASSWORD': 'secret',
            'HOST': 'DESKTOP-FF51PBJ',
            'PORT': '1433',

            'OPTIONS': {
                'driver': 'ODBC Driver 17 for SQL Server',
            },
        },
}

REST_FRAMEWORK = {
    # 'DEFAULT_RENDERER_CLASSES': [
    # 'rest_framework.renderers.JSONRenderer',
    # 'rest_framework.renderers.BrowsableAPIRenderer',
    # ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'NON_FIELD_ERRORS_KEY': 'Error',
     'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}


SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(hours=1),
    'REFRESH_TOKEN_LIFETIME': datetime.timedelta(days=1),
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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

# AUTH_USER_MODEL = 'users.UserAccounts'
AUTH_USER_MODEL = 'authentication.User'

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'frontend/build/static'),
    os.path.join(BASE_DIR, 'static'),
]

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
EMAIL_USE_TLS= True
EMAIL_HOST=os.environ.get('EMAIL_HOST')
EMAIL_PORT=os.environ.get('EMAIL_PORT')
EMAIL_HOST_USER=os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD=os.environ.get('EMAIL_HOST_PASSWORD') 

############################### LDAP Settings #####################
# Baseline configuration.
AUTH_LDAP_SERVER_URI = os.environ.get('LDAP_HOST_URI')

AUTH_LDAP_BIND_DN = "cn=admin,ou=users,ou=system"
AUTH_LDAP_BIND_PASSWORD = "1234"
AUTH_LDAP_USER_SEARCH = LDAPSearch(
    "ou=users,ou=system", ldap.SCOPE_SUBTREE, "(cn=%(user)s)"
)
# Or:
# AUTH_LDAP_USER_DN_TEMPLATE = 'uid=%(user)s,ou=users,dc=example,dc=com'

# Set up the basic group parameters.
# AUTH_LDAP_GROUP_SEARCH = LDAPSearch(
#     "ou=django,ou=groups,dc=example,dc=com",
#     ldap.SCOPE_SUBTREE,
#     "(objectClass=groupOfNames)",
# )
# AUTH_LDAP_GROUP_TYPE = GroupOfNamesType(name_attr="cn")

# # Simple group restrictions
# AUTH_LDAP_REQUIRE_GROUP = "cn=enabled,ou=django,ou=groups,dc=example,dc=com"
# AUTH_LDAP_DENY_GROUP = "cn=disabled,ou=django,ou=groups,dc=example,dc=com"

# Populate the Django user from the LDAP directory.
AUTH_LDAP_USER_ATTR_MAP = {
    "username": "cn",
    "email": "mail",
    "employeeID" : "employeeNumber"
}

# AUTH_LDAP_USER_FLAGS_BY_GROUP = {
#     "is_active": "cn=active,ou=django,ou=groups,dc=example,dc=com",
#     "is_staff": "cn=staff,ou=django,ou=groups,dc=example,dc=com",
#     "is_superuser": "cn=superuser,ou=django,ou=groups,dc=example,dc=com",
# }

# This is the default, but I like to be explicit.
AUTH_LDAP_ALWAYS_UPDATE_USER = True #True

# Use LDAP group membership to calculate group permissions.
# AUTH_LDAP_FIND_GROUP_PERMS = True

# Cache distinguished names and group memberships for an hour to minimize
# LDAP traffic.
AUTH_LDAP_CACHE_TIMEOUT = 3600

# Keep ModelBackend around for per-user permissions and maybe a local
# superuser.
AUTHENTICATION_BACKENDS = (
    "django_auth_ldap.backend.LDAPBackend",
    "django.contrib.auth.backends.ModelBackend",
)

