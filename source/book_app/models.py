from contextlib import nullcontext
from tabnanny import verbose
from django.db import models

from django.db.models import TextChoices

class Choices(models.TextChoices):
    ACTIVE = 'ACTIVE', 'Активная'
    BLOCKED = 'BLOCKED', 'Заблокировано'

class Record(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=200, null=False, blank=False)
    email = models.EmailField(verbose_name='e-mail', max_length=200, null=False, blank=False)
    text = models.TextField(verbose_name='Текст Записи', max_length=2000, null=False, blank=False)
    created_at = models.DateTimeField(verbose_name='Дата созадния', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='Дата редактирования', auto_now=True)
    status = models.CharField(verbose_name='Статус', max_length=20, choices=Choices.choices, default=Choices.ACTIVE)

    def __str__(self) -> str:
        return f'Name - {self.name}, email - {self.email}, text - {self.text}, created - {self.created_at}'
