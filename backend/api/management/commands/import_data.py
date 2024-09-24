import json
import uuid
import os
from datetime import datetime

import requests

from django.core.management.base import BaseCommand

from api.models import Log


class Command(BaseCommand):
    """
    Scans logs file from URL and saves records into DB
    example: ./manage.py import_data --url <URL>
    """
    def parse_url(self, url):
        """
        Checks if the file is on Google drive, return file's download link
        """
        if 'drive.google.com' in url:
            file_id = url.split('/')[5]
            return f'https://docs.google.com/uc?export=download&id={file_id}'
        return url

    def add_arguments(self, parser):
        parser.add_argument('--url', action='append', type=str)

    def handle(self, *args, **options):
        url: str = options.get('url')

        if not url:
            raise ValueError('URL must be provided!')
        url: str = self.parse_url(url[0])

        data = requests.get(url)

        tmp_file = f'/tmp/{uuid.uuid4()}'

        with open(tmp_file, 'wb') as file:
            file.write(data.content)

        for line in open(str(tmp_file)):
            line = json.loads(line)
            data = dict(
                remote_ip=line['remote_ip'],
                time=datetime.strptime(line['time'], '%d/%b/%Y:%H:%M:%S %z'),
                method=line['request'].split(' ')[0],
                url=line['request'].split(' ')[1],
                response=line['response'],
                bytes=line['bytes']
            )
            Log.objects.create(**data)

        os.remove(str(tmp_file))
