from django.utils.six import BytesIO
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from status.api.serializers import StatusSerializer
from status.models import Status


"""Serialize an object"""
obj = Status.objects.first()
serializer = StatusSerializer(obj)
json_data = JSONRenderer().render(serializer.data)
print(json_data)

stream = BytesIO(json_data)
data = JSONParser().parse(stream)
print(data)


"""Serialize queryset"""
qs = Status.objects.all()
serializer = StatusSerializer(qs, many=True)
json_data = JSONRenderer().render(serializer.data)
print(json_data)

stream = BytesIO(json_data)
data = JSONParser().parse(stream)
print(data)


"""Create object"""
data = {'user':1}
serializer = StatusSerializer(data=data)
serializer.is_valid()
serializer.save()



"""Update object"""
obj = Status.objects.first()
data = {'content': 'Some new content', 'user': 1}
update_serializer = StatusSerializer(obj, data=data)
if update_serializer.is_valid():
    update_serializer.save()



"""Delete object"""
data = {'user': 1, 'content': 'Will be deleted now'}
create_obj_serializer = StatusSerializer(data=data)
create_obj_serializer.is_valid()
created_obj = create_obj_serializer.save()  # Instance of obj
print(created_obj)


obj = Status.objects.last()
obj.delete()


"""Custom serializer"""
from rest_framework import serializers

class CustomSerializer(serializers.Serializer):
    content = serializers.CharField()
    email = serializers.EmailField

data = {'email': 'hello@gmail.com',
        'content': 'Will be deleted now'}
create_obj_serializer = CustomSerializer(data=data)
create_obj_serializer.is_valid()
created_obj = create_obj_serializer.save()  # Instance of obj
print(created_obj)
