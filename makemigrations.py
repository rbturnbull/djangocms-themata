#!/usr/bin/env python3

import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tests.settings")
    from django.core.management import execute_from_command_line
    args = sys.argv + ["makemigrations", "--empty", "djangocms_themata"]
    execute_from_command_line(args)

