""" Core App config
"""
from django.apps import AppConfig
from django.core.management import call_command


class CoreConfig(AppConfig):
    """Core App config"""

    default_auto_field = "django.db.models.BigAutoField"
    name = "barda.core"

    # * create default rule and admin
    def ready(self):
        call_command("create_rule_admin")
