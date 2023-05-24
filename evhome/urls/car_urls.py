from django.urls import path
from ..views.car import CarBrandListView, CarModelListView

urlpatterns = [
    path('car_brand/', CarBrandListView.as_view(), name='car_brand'),
    path('car_model/', CarModelListView.as_view(), name='car_model'),
]
