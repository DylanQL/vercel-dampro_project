from .settings import *
import os

# Configuraciones de seguridad para producción
DEBUG = False
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-d2&96j)tfe_dbif-g6@&&6tmu@7)#zqh0tj0nqnb8)#i^6n7i0')

# Hosts permitidos
ALLOWED_HOSTS = ['127.0.0.1', '.vercel.app', '.now.sh', 'localhost']

# Configuraciones de seguridad HTTPS (comentadas para desarrollo)
# SECURE_HSTS_SECONDS = 31536000
# SECURE_SSL_REDIRECT = True
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True

# Configuraciones de archivos estáticos para Vercel
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'system/static'),
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Configuración de base de datos (SQLite para simplicidad)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/tmp/db.sqlite3',  # Usar directorio temporal en Vercel
    }
}
