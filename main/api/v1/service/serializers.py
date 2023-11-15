from rest_framework import serializers
from service.models import QueryHistory


class QueryHistorySerializer(serializers.ModelSerializer):
    """Сериализатор для GET запроса"""
    class Meta:
        model = QueryHistory
        fields = ['cadastral_number', 'latitude', 'longitude', 'request_time', 'response']


class QueryHistoryCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для POST запроса"""
    class Meta:
        model = QueryHistory
        fields = ['cadastral_number', 'latitude', 'longitude']

class QueryResultSerializer(serializers.Serializer):
    """Сериализатор для эндпоинта /result"""
    query_id = serializers.IntegerField()
    response = serializers.BooleanField()
