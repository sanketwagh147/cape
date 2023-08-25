import os

EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_USE_SSL = os.environ.get('EMAIL_USE_SSL') == "True"
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS') == "True"
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_BACKEND = os.environ.get('EMAIL_BACKEND')
EMAIL_PORT = int(os.environ.get('EMAIL_PORT'))
EMAIL_HOST = os.environ.get('EMAIL_HOST')