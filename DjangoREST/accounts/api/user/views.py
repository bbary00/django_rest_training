from django.contrib.auth import get_user_model
from .serializers import UserDetailSerializer
from rest_framework import generics, pagination
from status.api.serializers import StatusInlineUserSerializer
from status.models import Status

User = get_user_model()


class UserDetailAPIView(generics.RetrieveAPIView):
    serializer_class = UserDetailSerializer
    queryset = User.objects.filter(is_active=True)
    lookup_field = 'username'



class UserStatusAPIView(generics.ListAPIView):
    serializer_class = StatusInlineUserSerializer
    # pagination_class = CustomPagination

    def get_serializer_context(self):
        return {'request': self.request}

    def get_queryset(self, *args, **kwargs):
        username = self.kwargs.get('username', None)
        if not username:
            return Status.objects.none()
        return Status.objects.filter(user__username=username)