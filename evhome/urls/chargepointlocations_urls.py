from django.urls import path
from ..views import ChargePointLocationsListView

urlpatterns = [
    path('', ChargePointLocationsListView.as_view(), name='charge_point_locations'),
]
