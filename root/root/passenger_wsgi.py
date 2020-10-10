import sys, os
from django.core.wsgi import get_wsgi_application


sys.path.append(os.getcwd())

os.environ['DJANGO_SETTINGS_MODULE'] = "root.settings"  # Nazwa modułu z ustawieniami

application = get_wsgi_application()