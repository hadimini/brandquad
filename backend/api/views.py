from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import no_body, swagger_auto_schema
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.filters import OrderingFilter

from api.models import Log
from api.serializers import ListSerializer, DetailSerializer
from api.filters.LogFilter import LogFilter


class ListView(ListAPIView):
    queryset = Log.objects.all()
    serializer_class = ListSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = LogFilter

    ordering_fields = ('pk', 'remote_ip', 'time', 'method', 'response', 'bytes')
    ordering = ('-pk',)

    @swagger_auto_schema(
        operation_summary='Log list',
        request_body=no_body,
        responses={200: ListSerializer()}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class DetailView(RetrieveAPIView):
    queryset = Log.objects.get_queryset()
    serializer_class = DetailSerializer

    @swagger_auto_schema(
        operation_summary='Log Detail',
        request_body=no_body,
        responses={200: DetailSerializer()}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
