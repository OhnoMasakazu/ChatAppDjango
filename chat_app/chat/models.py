from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.
class User(AbstractUser, models.Model):
    icon = models.ImageField(
        upload_to='img',
        verbose_name='image',
        blank=True,
    )

class TalkHistory(models.Model):
    text = models.CharField(max_length=200)
    date = models.DateTimeField(default=timezone.now)
    sender = models.CharField(max_length=100)
    receiver = models.CharField(max_length=100)