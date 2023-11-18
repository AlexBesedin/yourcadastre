import time  
import random
from celery import shared_task


@shared_task
def process_query(query_id):
    """Сelery задача, которая имитирует ответ сервера на """
    time.sleep(random.randint(0, 60)) 
    response = random.choice([True,])
    
    from service.models import QueryHistory
    query_instance = QueryHistory.objects.get(id=query_id)
    query_instance.response = response
    query_instance.save()
