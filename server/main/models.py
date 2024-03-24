from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15, verbose_name='phone', unique=True, error_messages="Enter your phone number", null=True)
    rights = models.IntegerField(verbose_name='rights', error_messages="Enter your phone number", null=True)

    def get_absolute_url(self):
        return reverse('user_detail', kwargs={'pk' : self.pk})