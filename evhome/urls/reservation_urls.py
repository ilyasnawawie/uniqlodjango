from django.urls import path
from ..views.reservation import *

urlpatterns = [
    path("reservations/", ReservationsListView.as_view(), name="reservations"),
    path("reservations_status/", ReservationsStatusListView.as_view(), name="reservations_status"),
    path("reservations_status_types/", ReservationsStatusTypesListView.as_view(), name="reservations_status_types"),
    path("reservations_order_relations/", ReservationsOrderRelationsListView.as_view(), name="reservations_order_relations"),
]
