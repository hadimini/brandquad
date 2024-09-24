from datetime import datetime

from rest_framework.test import APIClient

from django.test import TestCase
from django.urls import reverse

from api.models import Log


class TestLogDetail(TestCase):

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

    def test_detail(self):
        url = reverse('api:log_detail', args=[self.log.pk])
        response = self.api_client.get(url)
        r_data = response.data
        self.assertEqual(self.log.pk, r_data['pk'])
        self.assertEqual(self.log.remote_ip, r_data['remote_ip'])
        self.assertEqual(self.log.method, r_data['method'])
        self.assertEqual(self.log.url, r_data['url'])
        self.assertEqual(self.log.response, r_data['response'])
        self.assertEqual(self.log.bytes, r_data['bytes'])

    @classmethod
    def tearDownClass(cls):
        Log.objects.all().delete()