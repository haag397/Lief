"""create default rule for local admin and create default admin
"""

from django.core.management.base import BaseCommand
from barda.app.models import AdminData, Rules
from django.db import DatabaseError
import time


def check_table_exists(model_name):
    """Checks if a table for the specified model exists in the database."""

    try:
        model_name.objects.exists()
        return True
    except DatabaseError:
        return False


class Command(BaseCommand):
    """Django management command to create a default rule and admin if do not exist"""

    help = "Create a default rule and admin"

    def handle(self, *args, **kwargs):
        # * wait to table created
        time.sleep(4)

        # * Check if the Rules table exists
        if check_table_exists(Rules):
            if not Rules.objects.filter(rule_name="Owner").exists():
                # * Create a rule if it does not exist
                Rules.objects.create(
                    rule_name="Owner",
                    description="can write or edit or delete admins and edit settings",
                )
                self.stdout.write(
                    self.style.SUCCESS("Successfully created a new Owner")
                )
            else:
                self.stdout.write(self.style.WARNING("Rule already exists"))
        else:
            print("Rule table does not exist.")

        rule_ins = Rules.objects.get(rule_name="Owner")
        print(rule_ins.id)
        # * Check if the AdminData table exists
        if check_table_exists(AdminData):
            print("Admin table exist.")
            if not AdminData.objects.filter(username="hawork").exists():
                # * Create a admin if it does not exist
                AdminData.objects.create(
                    username="hawork",
                    password="zxcZ@123",
                    email="aghili@work.co",
                    last_name="eze",
                    rule_id=rule_ins,
                )
                self.stdout.write(
                    self.style.SUCCESS("Successfully created a new admin")
                )
            else:
                self.stdout.write(self.style.WARNING("Admin already exists"))
        else:
            print("Admin table does not exist.")
