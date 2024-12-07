from ._base import *  # noqa: F401 , F403
import os

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("POSTGRES_DB", "my_db"),
        "USER": os.getenv("POSTGRES_USER", "my_user"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD", "my_password"),
        "HOST": os.getenv("HOST", "db"),
        "PORT": os.getenv("PORT", "5432"),
    }
}


CORS_ORIGIN_ALLOW_ALL = True
CSRF_TRUSTED_ORIGINS = ["http://*", "https://*"]
CORS_ALLOW_HEADERS = [
    "accept",
    "referer",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-sessionid",
    "x-requested-with",
]
CORS_EXPOSE_HEADERS = ["Set-Cookie"]


DEBUG = False


AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")
AWS_S3_ENDPOINT_URL = os.getenv("AWS_S3_ENDPOINT_URL")
AWS_DEFAULT_ACL = 'public-read'
# Configuração de URLs
AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.{AWS_S3_ENDPOINT_URL}"

# Definir como backend de armazenamento padrão
DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"