"""
Test custom managemnt commands
"""
from unittest.mock import patch

from psycopg2 import OperationalError as Psycopg2Error

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase

@patch('core.management.commands.wait_for_db.Command.check')
class CommandTests(SimpleTestCase):
    """
    Test commands
    """
    def test_wait_for_db_ready(self,patch_check):
        """Test waiting for database to if database ready"""
        patch_check.return_value = True # patch the command check method of Base command

        call_command('wait_for_db')

        patch_check.assert_called_once_with(databases=['default']) # test if the command is called with this database

    @patch('time.sleep')
    def test_wait_for_db_delay(self,patch_sleep,patch_check):
        """test waiting for database when getting OperationalError"""
        patch_check.side_effect = [Psycopg2Error]*2+ [OperationalError]*2+[True]#first two  times call Psycopg2Error

        call_command('wait_for_db')

        self.assertEqual(patch_check.call_count,6) #test if the database was called 6 times

        patch_check.assert_called_with(databases=['default'])


