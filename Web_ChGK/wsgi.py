"""
WSGI config for Web_ChGK project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
import sys
sys.path.append('PycharmProjects\TryWebOnDjango\Web_ChGK')
sys.path.append('PycharmProjects\TryWebOnDjango\Web_ChGK\Web_ChGK')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Web_ChGK.settings')

application = get_wsgi_application()
