from django.urls import path
from ..views import CarModelListView

urlpatterns = [
    path('car_model/', CarModelListView.as_view(), name='car_model'),
]
