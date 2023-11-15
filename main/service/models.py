from django.db import models

from .validators import validate_cadastral_number, validate_latitude, validate_longitude


class QueryHistory(models.Model):
    """Класс модели запроса"""
    cadastral_number = models.CharField(
        max_length=100,
        verbose_name='Кадастровый номер',
        validators=[validate_cadastral_number])
    latitude = models.FloatField(
        verbose_name='Широта',
        validators=[validate_latitude])
    longitude = models.FloatField(
        verbose_name='Долгота',
        validators=[validate_longitude])
    request_time = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата запроса')
    response = models.BooleanField(null=True, blank=True)


    class Meta:
        verbose_name = "История запросов"

    def __str__(self):
        return f"Кадастровый номер: {self.cadastral_number} Дата запроса: {self.request_time}"
