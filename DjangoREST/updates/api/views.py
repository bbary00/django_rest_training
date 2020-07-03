from updates.models import Update as UpdateModel
from django.http import HttpResponse
from django.views.generic import View
from .mixins import CSEFExemptMixin
from djrest.mixins import HttpResponseMixin
from updates.forms import UpdateModelForm
from .utils import is_json
import json


class UpdateModelDetailAPIView(HttpResponseMixin, CSEFExemptMixin, View):

    """
    Retrieve Update Delete
    """
    is_json = True

    def get_object(self, id=None):
        qs = UpdateModel.class_objects.filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None

    def get(self, request, id, *args, **kwargs):
        obj = self.get_object(id=id)
        if not obj:
            error_data = json.dumps({'message': 'Update not found'})
            return self.render_to_response(error_data, status=404)
        json_data = obj.serialize_class_object()
        return self.render_to_response(json_data)

    def post(self, request, *args, **kwargs):
        data = {
            'status': 'NOT_OK'
        }
        json_data = json.dumps(data)
        return self.render_to_response(json_data)

    def put(self, request, id, *args, **kwargs):
        # Check if sent data is json
        if not is_json(request.body):
            error_data = json.dumps({'message': 'Wrong data format. Please use JSON instead.'})
            return self.render_to_response(error_data, status=400)

        # Check if object with this id exists
        obj = self.get_object(id=id)
        if not obj:
            error_data = json.dumps({'message': 'Object not found'})
            return self.render_to_response(error_data, status=404)

        data = json.loads(obj.serialize_class_object())
        passed_data = json.loads(request.body)
        for k, v in passed_data.items():
            data[k] = v

        form = UpdateModelForm(data, instance=obj)
        if form.is_valid():
            obj = form.save(commit=True)
            json_data = json.dumps(data)
            return self.render_to_response(json_data, status=201)
        else:
            json_data = json.dumps(form.errors)
            return self.render_to_response(json_data, status=400)

    def delete(self, request, id, *args, **kwargs):
        # Check if object with this id exists
        obj = self.get_object(id=id)
        if not obj:
            error_data = json.dumps({'message': 'Object not found'})
            return self.render_to_response(error_data, status=404)
        deleted = obj.delete()
        print(deleted)
        json_data = json.dumps({'message': 'Successfully deleted'})
        return self.render_to_response(json_data)


class UpdateModelListAPIView(HttpResponseMixin, CSEFExemptMixin, View):

    """
    List view
    Create view
    """

    is_json = True
    queryset = None

    def get_queryset(self):
        qs = UpdateModel.class_objects.all()
        self.queryset = qs
        return qs

    def get_object(self, id=None):
        if not id:
            return None

        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None

    def get(self, request, *args, **kwargs):
        data = json.loads(request.body)
        passed_id = data.get('id', None)
        if passed_id:
            obj = self.get_object(id=passed_id)
            if not obj:
                error_data = json.dumps({'message': 'Update not found'})
                return self.render_to_response(error_data, status=404)
            json_data = obj.serialize_class_object()
            return self.render_to_response(json_data)
        else:
            qs = self.get_queryset()
            json_data = qs.serialize_data()
            return self.render_to_response(json_data, status=400)

    def post(self, request, *args, **kwargs):
        # Check if sent data is json
        if not is_json(request.body):
            error_data = json.dumps({'message': 'Wrong data format. Please use JSON instead.'})
            return self.render_to_response(error_data, status=400)

        data = json.loads(request.body)
        form = UpdateModelForm(data)
        if form.is_valid():
            obj = form.save(commit=True)
            json_data = obj.serialize_class_object()
            return self.render_to_response(json_data, status=201)
        else:
            json_data = json.dumps(form.errors)
            return self.render_to_response(json_data, status=400)

    # def delete(self, request, *args, **kwargs):
    #     data = {
    #         'status': 'You can\'t delete this'
    #     }
    #     json_data = json.dumps(data)
    #     return self.render_to_response(json_data, status=403)

    def put(self, request, *args, **kwargs):
        # Check if sent data is json
        if not is_json(request.body):
            error_data = json.dumps({'message': 'Wrong data format. Please use JSON instead.'})
            return self.render_to_response(error_data, status=400)
        passed_data = json.loads(request.body)
        passed_id = passed_data.get('id', None)
        if not passed_id:
            error_data = json.dumps({'id': 'Please specify which id to delete.'})
            return self.render_to_response(error_data, status=400)

        # Check if object with this id exists
        obj = self.get_object(id=passed_id)
        if not obj:
            error_data = json.dumps({'message': 'Object not found'})
            return self.render_to_response(error_data, status=404)

        data = json.loads(obj.serialize_class_object())

        for k, v in passed_data.items():
            data[k] = v

        form = UpdateModelForm(data, instance=obj)
        if form.is_valid():
            obj = form.save(commit=True)
            json_data = json.dumps(data)
            return self.render_to_response(json_data, status=201)
        else:
            json_data = json.dumps(form.errors)
            return self.render_to_response(json_data, status=400)

    def delete(self, request, *args, **kwargs):
        # Check if sent data is json
        if not is_json(request.body):
            error_data = json.dumps({'message': 'Wrong data format. Please use JSON instead.'})
            return self.render_to_response(error_data, status=400)
        passed_data = json.loads(request.body)
        passed_id = passed_data.get('id', None)

        # Check if object with this id exists
        obj = self.get_object(id=passed_id)
        if not obj:
            error_data = json.dumps({'message': 'Object not found'})
            return self.render_to_response(error_data, status=404)


        deleted = obj.delete()
        print(deleted)
        json_data = json.dumps({'message': 'Successfully deleted'})
        return self.render_to_response(json_data)


