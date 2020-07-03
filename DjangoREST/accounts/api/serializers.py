from rest_framework import generics
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_jwt.settings import api_settings
from django.utils import timezone
import datetime


jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER
expires_delta = api_settings.JWT_REFRESH_EXPIRATION_DELTA

User = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):
    password_confirmation = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    token = serializers.SerializerMethodField(read_only=True)
    expires = serializers.SerializerMethodField(read_only=True)
    # token_response = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'password_confirmation',
            'token',
            'expires',
            # 'token_response'
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, attrs):
        pw_first = attrs.get('password')
        pw_second = attrs.pop('password_confirmation')
        if pw_first != pw_second:
            raise serializers.ValidationError("Passwords must match")
        return attrs

    def validate_email(self, email):
        qs = User.objects.filter(email__iexact=email)
        if qs.exists():
            raise serializers.ValidationError('User with this email already exists!')
        return email

    def get_token(self, user):
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return token

    def get_expires(self, user):
        return timezone.now() + expires_delta - datetime.timedelta(seconds=200)

    # def get_token_response(self, user):
    #     payload = jwt_payload_handler(user)
    #     token = jwt_encode_handler(payload)
    #     context = self.context
    #     response = jwt_response_payload_handler(token, user, request=context['request'])
    #     return response

    def validate_username(self, username):
        qs = User.objects.filter(username__iexact=username)
        if qs.exists():
            raise serializers.ValidationError('User with this username already exists!')
        return username

    def create(self, validated_data):
        user_obj = User.objects.create(username=validated_data.get('username'),
                                       email=validated_data.get('email'))
        user_obj.set_password(validated_data.get('password'))
        user_obj.save()
        return user_obj
