from django.urls import path
from .views import (update_model_detail_view,
                    JsonCBV,
                    JsonCBV2,
                    SerializedView,
                    SerializedListView)

urlpatterns = [
    path('test', update_model_detail_view, name='update_model_datail_view'),
    path('cbv', JsonCBV.as_view(), name='JsonCBV'),
    path('cbv2', JsonCBV2.as_view(), name='JsonCBV2'),
    path('ser', SerializedView.as_view(), name='SerializedView'),
    path('ser_list', SerializedListView.as_view(), name='SerializedListView')
]
