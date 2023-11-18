import random
import time
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

from service.tasks import process_query
from service.models import QueryHistory
from .serializers import QueryHistorySerializer, QueryHistoryCreateSerializer, QueryResultSerializer


@api_view(['GET'])
def history(request):
    """GET запрос, выдающий историю запросов"""
    cadastral_number = request.query_params.get('cadastral_number')
    if cadastral_number:
        queries = QueryHistory.objects.filter(cadastral_number=cadastral_number)
    else:
        queries = QueryHistory.objects.all()
    serializer = QueryHistorySerializer(queries, many=True)
    return Response(serializer.data)


@swagger_auto_schema(methods=['post'], request_body=QueryHistoryCreateSerializer)
@api_view(['POST'])
def query(request):
    serializer = QueryHistoryCreateSerializer(data=request.data)
    if serializer.is_valid():
        query_instance = serializer.save(response=None)
        process_query.delay(query_instance.id)
        return Response({'status': 'Запрос получен, ожидайте ответа сервера.', 'query_id': query_instance.id})
    return Response(serializer.errors, status=400)


@swagger_auto_schema(methods=['post'], request_body=QueryResultSerializer)
@api_view(['POST'])
def result(request):
    serializer = QueryResultSerializer(data=request.data)
    if serializer.is_valid():
        query_id = serializer.validated_data['query_id']
        response = serializer.validated_data['response']

        try:
            query_instance = QueryHistory.objects.get(id=query_id)
            query_instance.response = response
            query_instance.save()
            return Response({'status': 'успешно'})
        except QueryHistory.DoesNotExist:
            return Response({'error': 'Query not found'}, status=404)

    return Response(serializer.errors, status=400)



@api_view(['GET'])
def ping(request):
    return Response({"message": "Сервер запущен"})
