import os
from django.core.management import execute_from_command_line

os.environ['DJANGO_SETTINGS_MODULE'] = 'uniqlo.settings'  # replace 'myproject.settings' with your settings module

if __name__ == "__main__":
    execute_from_command_line([
        "manage.py",
        "runserver_plus",
        "443",
        "--cert-file", "cert.pem",
        "--key-file", "key.pem",
    ])