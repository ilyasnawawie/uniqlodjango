from django.urls import path
from ..views.charge_point import *

urlpatterns = [
    path(
        "charge_point_locations/",
        ChargePointLocationsListView.as_view(),
        name="charge_point_locations",
    ),
    path(
        "charge_point_location_ownerships/",
        ChargePointLocationsOwnershipsListView.as_view(),
        name="charge_location_ownerships",
    ),
    path("charge_point/",
         ChargePointListView.as_view(),
         name="charge_point"),
]
