from django.db import models
from users.models import CustomUser
from sections.models import Section

class Schedule(models.Model):
    date = models.DateField(verbose_name="Дата проведения")
    time = models.TimeField(verbose_name="Время проведения")
    section = models.ForeignKey(Section, on_delete=models.PROTECT, verbose_name="Секция")
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT)