from rest_framework import serializers
from django.contrib.auth import get_user_model
from status.api.serializers import StatusInlineUserSerializer
from rest_framework.reverse import reverse as api_reverse

User = get_user_model()


class UserDetailSerializer(serializers.ModelSerializer):
    user_uri = serializers.SerializerMethodField(read_only=True)
    status = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'user_uri',
            'status'
        ]

    def get_user_uri(self, obj):
        request = self.context.get('request')
        return api_reverse('detail', kwargs={'username': obj.username}, request=request)

    def get_status(self, obj):
        request = self.context.get('request')
        data = {
            'uri': self.get_user_uri(obj) + 'status/',
            'recent_statuses': self.get_resent_status(obj, request)
        }
        return data

    def get_resent_status(self, obj, request):
        qs = obj.status_set.all().order_by('-timestamp')
        return StatusInlineUserSerializer(qs, many=True, context={'request': request}).data
