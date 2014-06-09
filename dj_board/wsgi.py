import os
import sys

sys.path.append("D:/dev/python/web/dj_board")
os.environ['DJANGO_SETTINGS_MODULE'] = 'dj_board.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
