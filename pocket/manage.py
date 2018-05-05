#!/usr/bin/env python
import os
import sys

from django.conf import settings

if __name__ == "__main__":
    deployment = os.getenv('ENV', 'DEBUG')
    if deployment == 'DEBUG':
        os.environ.setdefault(
            "DJANGO_SETTINGS_MODULE",
            "config.development.settings"
        )
    else:
        raise NotImplementedError('PRODUCTION not implemented')

    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
