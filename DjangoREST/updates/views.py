from django.http import JsonResponse, HttpResponse
from django.core.serializers import serialize
from django.views.generic import View
from djrest.mixins import JsonResponseMixin
from django.shortcuts import render
from .models import Update
import json


# def detail_view(request):
#     return render() # return JSON data

def update_model_detail_view(request):
    """
    URI
    """
    data = {
        'cout': 1000,
        'counter': 'Some content'
    }
    return JsonResponse(data)


class JsonCBV(View):

    @staticmethod
    def get(request, *args, **kwargs):
        data = {
            'cout': 1000,
            'counter': 'Some content'
        }
        return JsonResponse(data)


class JsonCBV2(JsonResponseMixin, View):

    def get(self, request, *args, **kwargs):
        data = {
            'cout': 1000,
            'counter': 'Some content'
        }
        return self.render_to_json_response(data)


class SerializedView(JsonResponseMixin, View):

    @staticmethod
    def get(request, *args, **kwargs):
        obj = Update.class_objects.get(id=1)
        json_data = obj.serialize_class_object()
        return HttpResponse(json_data, content_type='application/json')

# class SerializedView(MixedView):
#
#     def get_context(self, request):
#         context = dict()
#         context['updates'] = Update.class_objects.all()
#         return context
#
#     template_name = 'publisher_list.html'
#
#     def convert_context_to_json(self, context):
#         json_context = dict()
#         json_context['publisher_names'] = [p.name for p in context['publishers']]
#         return json.dumps(json_context, encoding='utf-8', ensure_ascii=False)


class SerializedListView(JsonResponseMixin, View):

    @staticmethod
    def get(request, *args, **kwargs):
        json_data = Update.class_objects.all().serialize_data()
        return HttpResponse(json_data, content_type='application/json')
