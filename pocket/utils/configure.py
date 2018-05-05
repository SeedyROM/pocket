import os
import sys

from django.conf import settings


deployment = os.getenv('ENV', 'DEBUG')
if deployment == 'DEBUG':
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        "config.development.settings"
    )
else:
    raise NotImplementedError('PRODUCTION not implemented')