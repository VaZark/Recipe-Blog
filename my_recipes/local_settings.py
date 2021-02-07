# CORS_SETUP

CORS_APP = ['corsheaders']
CORS_MIDDLEWARE = [ 
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware'
]
CORS_ORIGIN_ALLOW_ALL = True