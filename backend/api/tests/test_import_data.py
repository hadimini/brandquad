import os

import requests_mock

from django.core.management import call_command
from django.test import TestCase

from api.models import Log


class TestImportData(TestCase):
    def load_fixture(self, filename):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(dir_path, 'fixtures', filename)

        with open(file_path) as f:
            return f.read()

    def setUp(self) -> None:
        super().setUp()
        self.url = 'https://example.com/data.txt'

    def test_import_data_command(self):

        #
        with requests_mock.Mocker() as m:
            m.register_uri(
                'GET',
                self.url,
                text=self.load_fixture('test_logs_data.txt'),
                status_code=200,
            )

            self.assertEqual(0, Log.objects.count())
            options = {'url': [self.url]}
            call_command('import_data', [], **options)
            self.assertEqual(3, Log.objects.count())

            self.assertEqual('80.91.33.133', Log.objects.last().remote_ip)

    def tearDown(self) -> None:
        super().tearDown()
