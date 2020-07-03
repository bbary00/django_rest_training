from django.core.serializers import serialize
from django.conf import settings
from django.db import models
import json


def upload_update_image(instance, filename):
    return f'update/{instance.user}/{filename}'


class UpdateQuerySet(models.QuerySet):

    # def serialize_data(self):
    #     return serialize('json', self, fields=('user', 'content', 'image'))

    # def serialize_data(self):
    #     json_array = []
    #     qs = self
    #     for obj in qs:
    #         struct = json.loads(obj.serialize_class_object())
    #         json_array.append(struct)
    #     return json.dumps(json_array)

    def serialize_data(self):
        list_values = list(self.values('id', 'user', 'content', 'image'))
        return json.dumps(list_values)


class UpdateManager(models.Manager):
    def get_queryset(self):
        return UpdateQuerySet(self.model, using=self._db)


class Update(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to=upload_update_image, blank=True, null=True)
    timestamp = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class_objects = UpdateManager()

    def __str__(self):
        return self.content or ''

    def serialize_class_object(self):

        data = {
            'id': self.id,
            'user': self.user.id,
            'content': self.content,
            'image': self.image.url if self.image else ''
        }
        data = json.dumps(data)
        return data

    # def serialize_class_object(self):
    #     json_data = serialize('json', [self], fields=('user', 'content', 'image'))
    #     struct = json.loads(json_data)
    #     data = json.dumps(struct[0]['fields'])
    #     return data
