# app config
API_KEY = "api_key"
API_SECRET = "secret_key"
# celery configuration 
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'