from django.db import models


class Log(models.Model):
    remote_ip = models.CharField(max_length=64)
    time = models.DateTimeField()
    method = models.CharField(max_length=12)
    url = models.TextField()
    response = models.IntegerField()
    bytes = models.IntegerField()
