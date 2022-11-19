"""
    Django command to wait for the database to be available
"""
from django.core.management.base import BaseCommand
from psycopg2 import OperationalError as Psyposg2Error
from django.db.utils import OperationalError
import time


class Command(BaseCommand):
    """Django command to wait for database"""

    def handle(self, *args, **options):
        """Entrypoint for command"""
        self.stdout.write("wait for database ......")
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psyposg2Error, OperationalError):
                self.stdout.write("database unavailable wait 1 second")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("Database available"))
