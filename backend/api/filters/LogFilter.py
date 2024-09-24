from django_filters import rest_framework as filters

from django.db.models import Q

from api.models import Log


class LogFilter(filters.FilterSet):
    search = filters.CharFilter(method='filter_search')

    def filter_search(self, queryset, name, value):
        if not value:
            return queryset
        return queryset.filter(Q(remote_ip__icontains=value) | Q(url__icontains=value))

    class Meta:
        model = Log
        fields = ('method', 'response', 'search', 'time')
