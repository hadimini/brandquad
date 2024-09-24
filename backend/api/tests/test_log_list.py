from rest_framework.test import APIClient

from django.test import TestCase
from django.urls import reverse

from api.models import Log


class TestLogList(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.api_client = APIClient()
        cls.log = Log.objects.create(
            remote_ip='11.11.11.123',
            time='2000-10-01 12:00:00',
            method='GET',
            url='/downloads/product_1',
            response=304,
            bytes=770
        )

    def test_list(self):
        url = reverse('api:log_list')
        response = self.api_client.get(url)
        r_data = response.data
        self.assertEqual(1, r_data['count'])
        results = r_data['results']
        self.assertEqual(self.log.pk, results[0]['pk'])
        self.assertEqual(self.log.remote_ip, results[0]['remote_ip'])
        self.assertEqual(self.log.method, results[0]['method'])
        self.assertEqual(self.log.url, results[0]['url'])
        self.assertEqual(self.log.response, results[0]['response'])
        self.assertEqual(self.log.bytes, results[0]['bytes'])

    @classmethod
    def tearDownClass(cls):
        Log.objects.all().delete()