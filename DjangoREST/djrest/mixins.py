from django.http import JsonResponse, HttpResponse
from django.views.generic import View, TemplateView


class HttpResponseMixin(object):
    is_json = False

    def render_to_response(self, content, status=200):
        if self.is_json:
            content_type = 'application/json'
        return HttpResponse(content, content_type=content_type, status=status)


class JsonResponseMixin(object):

    def render_to_json_response(self, content, **kwargs):
        return JsonResponse(self.get_data(content), **kwargs)

    def get_data(self, context):
        return context


# class MixedView(View, JsonResponseMixin, TemplateView):
#     def get_context(self, request):
#         pass
#
#     def get(self, request, *args, **kwargs):
#         context = self.get_context(request)
#         if request.GET.get('format', 'html') == 'json' or self.template_name is None:
#             return JsonResponseMixin.render_to_response(self, context)
#         else:
#             return TemplateView.render_to_response(self, context)