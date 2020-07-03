from django.db import models
from django.conf import settings
import json


def upload_update_image(instance, filename):
    return f'status/{instance.user}/{filename}'


class StatusQuerySet(models.QuerySet):
    def serialize_data(self):
        list_values = list(self.values('id', 'user', 'content', 'image'))
        return json.dumps(list_values)


class StatusManager(models.Manager):
    def get_queryset(self):
        return StatusQuerySet(self.model, using=self._db)


class Status(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to=upload_update_image, null=True, blank=True)
    timestamp = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.content)[:50]

    class Meta:
        verbose_name = 'Status post'
        verbose_name_plural = 'Status posts'

    @property
    def owner(self):
        return self.user
