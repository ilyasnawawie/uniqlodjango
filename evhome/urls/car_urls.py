from django.urls import path
from ..views.car import *

urlpatterns = [
    path("car_brand/", CarBrandListView.as_view(), name="car_brand"),
    path("car_model/", CarModelListView.as_view(), name="car_model"),
    path("user_car/", UserCarListView.as_view(), name="user_car"),
]
