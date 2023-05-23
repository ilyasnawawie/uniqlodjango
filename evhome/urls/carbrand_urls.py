from django.urls import path
from ..views import CarBrandListView

urlpatterns = [
    path('', CarBrandListView.as_view(), name='car_brand'),
]
