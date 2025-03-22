import sys, os

sys.path.insert(0, "/home/yadgahhi/yadgah")

os.environ['DJANGO_SETTINGS_MODULE'] = 'Yadgah.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
