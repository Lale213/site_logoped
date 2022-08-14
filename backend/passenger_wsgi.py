# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/home/r/rmyagka6/rmyagka6.beget.tech/backend')
sys.path.insert(1, '/home/r/rmyagka6.beget.tech/djangoenv/lib/python3.8/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'backend.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()