# tasks.py

from celery import shared_task
import time  # Для эмуляции задержки
import random  # Для генерации случайного ответа

@shared_task
def process_query(query_id):
    time.sleep(random.randint(0, 60))  # Симуляция задержки до 60 секунд
    response = random.choice([True, False])  # Случайный ответ True или False

    # Найти и обновить соответствующий QueryHistory объект
    from service.models import QueryHistory
    query_instance = QueryHistory.objects.get(id=query_id)
    query_instance.response = response
    query_instance.save()
