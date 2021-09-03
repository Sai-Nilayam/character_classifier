"""
WSGI config for test_site project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""
# Self added codes. This code is very important. If not added then the globally installed
# libapache2-mod-wsgi-py3 will not take the Vertual Environment and always show 'No module
# name django' error.

import sys
sys.path.insert(
    0, '/home/sai-nilayam/personal/dev/venvs/tf/lib/python3.7/site-packages')

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_site.settings')

application = get_wsgi_application()
