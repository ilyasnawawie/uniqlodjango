from django.urls import path
from ..views import ChargePointLocationsOwnershipsListView


urlpatterns = [
    path('', ChargePointLocationsOwnershipsListView.as_view(), name='charge_location_ownerships'),
]
