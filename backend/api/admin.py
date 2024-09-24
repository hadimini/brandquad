from rangefilter.filters import DateTimeRangeFilterBuilder

from django.contrib import admin

from api.models import Log


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    date_hierarchy = 'time'
    list_display = ['pk', 'remote_ip', 'time', 'method', 'url', 'response', 'bytes']
    list_filter = [('time', DateTimeRangeFilterBuilder()), 'method', 'response']
    search_fields = ['remote_ip', 'url']
    search_help_text = 'Search by IP, URL'
