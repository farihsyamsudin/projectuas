import os
from whitenoise import WhiteNoise
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projectuas.settings')

application = get_wsgi_application()

app = application

application = WhiteNoise(application)