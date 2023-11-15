from django.core.exceptions import ValidationError
import re


def validate_cadastral_number(value):
    """Валидация кадастрового номера"""
    pattern = r'^\d+:\d+:\d+:\d+$'
    if not re.match(pattern, value):
        raise ValidationError(
            f'{value} не является действительным кадастровым номером. Ожидаемый формат: XX:XX:XXXX:XXX')


def validate_latitude(value):
    """Валидация значения широта"""
    if not -90 <= value <= 90:
        raise ValidationError(
            f'Широта {value} находится вне допустимого диапазона (от -90 до 90)')


def validate_longitude(value):
    """Валидация значения долготы"""
    if not -180 <= value <= 180:
        raise ValidationError(
            f'Долгота {value} находится вне допустимого диапазона (от -180 до 180)')
