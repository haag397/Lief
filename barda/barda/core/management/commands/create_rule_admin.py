"""create default rule for local admin and create default admin
"""

from django.core.management.base import BaseCommand
from django.db import DatabaseError
from barda.core.models import AdminData, Rules


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
        # * check rules table exist
        while check_table_exists(Rules):

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
            break
        else:
            print("Rule table does not exist.")

        # * check admindata table exist
        while check_table_exists(AdminData):
            # * get rule instance for foreign key
            rule_ins = Rules.objects.get(rule_name="Owner")

            if not AdminData.objects.filter(username="hawork").exists():
                # * Create a admin if it does not exist
                AdminData.objects.create(
                    username="hawork",
                    password="zxcZ@123",
                    email="aghili@work.co",
                    last_name="eze",
                    rule_name=rule_ins,
                )
                self.stdout.write(
                    self.style.SUCCESS("Successfully created a new admin")
                )
            else:
                self.stdout.write(self.style.WARNING("Admin already exists"))
            break
        else:
            print("Admin table does not exist.")
