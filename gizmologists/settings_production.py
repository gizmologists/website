import os

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
DEBUG = False

ALLOWED_HOSTS = [
  ".gizmologists.com"
]

# AWS
AWS_ACCESS_KEY_ID = os.environ.get('GIZMOLOGISTS_AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('GIZMOLOGISTS_AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = 'gizmologists'

# Tell django-storages the domain to use to refer to static files.
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

# STATIC FILES
STATICFILES_STORAGE = 'custom_storages.StaticStorage'
MEDIAFILES_STORAGE = 'custom_storages.MediaStorage'

STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, 'static')
MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, 'media')

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_QUERYSTRING_AUTH = False

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
X_FRAME_OPTIONS = "DENY"

SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
# TODO: Reenable when SSL installed
#SECURE_SSL_REDIRECT = True
SECURE_SSL_REDIRECT = False

# TODO: Update to higher value like 31536000 when known OK
SECURE_HSTS_SECONDS = 3600
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
