from django.urls import path

from api.v1.service.views import history, ping, query, result


urlpatterns = [
    path('query/', query, name='query'),
    path('history/', history, name='history'),
    path('ping/', ping, name='ping'),
    path('result/', result, name='result')
]
