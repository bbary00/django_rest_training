from django.urls import path
from .views import (StatusAPIView,
                    StatusAPIDetailView,
                    # StatusCreateAPIView,
                    # StatusDetailAPIView,
                    # StatusUpdateAPIView,
                    # StatusDeleteAPIView)
                    )

urlpatterns = [
    path('', StatusAPIView.as_view(), name='StatusList'),
    path('<int:id>/', StatusAPIDetailView.as_view(), name='StatusId'),
    # path('create', StatusCreateAPIView.as_view(), name='StatusCreate'), # Commented because StatusAPIView now handle
    # path('<int:id>', StatusDetailAPIView.as_view(), name='StatusRetrieve'),
    # path('<int:id>/update', StatusUpdateAPIView.as_view(), name='JsonCBV'), # Commented these both because
    # path('<int:id>/delete', StatusDeleteAPIView.as_view(), name='JsonCBV'), # StatusDetailAPIView now handle them
]
