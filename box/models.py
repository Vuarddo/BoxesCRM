from django.conf import settings
from django.db import models
from django.utils import timezone

from django.db import models

class boxes(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    boxName = models.CharField(max_length=50)
    amountSm = models.IntegerField()
    vidpovid = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    text = models.CharField(max_length=50)
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
