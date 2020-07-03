from rest_framework import serializers
from status.models import Status
from rest_framework.reverse import reverse as api_reverse


class StatusSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Status
        fields = [
            'id',
            'user',
            'content',
            'image',
            'uri'
        ]
        read_only_fields = ['user']

    def get_uri(self, obj):
        request = self.context.get('request')
        return api_reverse('StatusId', kwargs={'id': obj.id}, request=request)


    # def validate_content(self, attrs):                                    # validate every field
    #     if len(attrs) > 256:
    #         raise serializers.ValidationError('Content is too long!')
    #     return attrs

    def validate(self, attrs):
        content = attrs.get('content', None)
        image = attrs.get('image', None)
        if not content and not image:
            raise serializers.ValidationError('Content or image is required!')
        return attrs


class StatusInlineUserSerializer(StatusSerializer):
    uri = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Status
        fields = [
            'id',
            'user',
            'content',
            'image',
            'uri'
        ]
        read_only_fields = ['user']


