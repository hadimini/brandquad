from rest_framework import serializers

from api.models import Log


class DetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Log
        fields = ('pk', 'remote_ip', 'time', 'method', 'url', 'response', 'bytes')


class ListSerializer(DetailSerializer):

    class Meta:
        model = Log
        fields = (*DetailSerializer.Meta.fields, )
