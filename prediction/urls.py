from django.urls import path
from .views import SpaceDetectView

urlpatterns = [
    path('predict/', SpaceDetectView.as_view(), name='predict_hazard'),
]
