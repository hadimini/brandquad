from django.urls import path

from backend.api.views import DetailView, ListView


urlpatterns = [
    path('', ListView.as_view(), name='log_list'),
    path('<int:pk>/', DetailView.as_view(), name='log_detail'),
]

app_name = 'api'
