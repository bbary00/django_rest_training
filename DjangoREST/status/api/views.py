from rest_framework.views import APIView
from rest_framework import generics, mixins, permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from rest_framework.authentication import SessionAuthentication     # for getting current session user but it
                                                                    # globally implemented in settings

from updates.api.utils import is_json
from .serializers import StatusSerializer
from status.models import Status
from accounts.api.permissions import IsOwnerOrReadOnly

import json


class StatusAPIDetailView(mixins.UpdateModelMixin,
                          mixins.DestroyModelMixin,
                          generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    lookup_field = 'id'

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class StatusAPIView(mixins.CreateModelMixin,
                    generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = StatusSerializer
    search_fields = ('user__username', 'content')
    passed_id = None
    queryset = Status.objects.all()

    # def get_queryset(self):
    #     qs = Status.objects.all()
    #     query = self.request.GET.get('q')
    #     if query:
    #         qs = qs.filter(content__icontains=query)
    #     return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)





    # def get_object(self):
    #     request = self.request
    #     passed_id = request.GET.get('id', None) or self.passed_id
    #     queryset = self.get_queryset()
    #     obj = None
    #     if queryset:
    #         obj = get_object_or_404(queryset, id=passed_id)
    #         self.check_object_permissions(request, obj)
    #     return obj

    # def get(self, request, *args, **kwargs):
    #     url_passed_id = request.GET.get('id', None)
    #     json_data = {}
    #     if is_json(request.body):
    #         json_data = json.loads(request.body)
    #
    #     passed_id = json_data.get('id', url_passed_id)
    #     self.passed_id = passed_id
    #     if passed_id:
    #         return self.retrieve(request, *args, **kwargs)
    #     return super().get(request, *args, **kwargs)

















# class StatusListSearchAPIView(APIView):
#     permission_classes = []
#     authentication_classes = []
#
#     def get(self, request, format=None):
#         qs = Status.objects.all()
#         serialized_data = StatusSerializer(qs, many=True)
#         return Response(serialized_data.data)


# class StatusAPIView(mixins.CreateModelMixin, generics.ListAPIView):  # Create List
#     permission_classes = []
#     authentication_classes = []
#     # queryset = Status.objects.all()
#     serializer_class = StatusSerializer
#
#     def get_queryset(self):
#         qs = Status.objects.all()
#         query = self.request.GET.get('q')
#         if query:
#             qs = qs.filter(content__icontains=query)
#         return qs
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)


# class StatusCreateAPIView(generics.CreateAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)


# class StatusDetailAPIView(mixins.UpdateModelMixin,
#                           mixins.DestroyModelMixin,
#                           generics.RetrieveAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
#     lookup_field = 'id'
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

    # def get_object(self, *args, **kwargs):
    #     kwargs = self.kwargs
    #     kw_id = kwargs.get('id', None)
    #     return Status.objects.get(id=kw_id)


# class StatusUpdateAPIView(generics.UpdateAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
#     lookup_field = 'id'
#
#
# class StatusDeleteAPIView(generics.DestroyAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
#     lookup_field = 'id'
