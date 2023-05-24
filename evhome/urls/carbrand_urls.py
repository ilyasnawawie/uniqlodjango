from django.urls import path
from ..views import CarBrandListView

urlpatterns = [
    path('car_brand/', CarBrandListView.as_view(), name='car_brand'),
]
