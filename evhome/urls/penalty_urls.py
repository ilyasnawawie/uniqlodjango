from django.urls import path
from ..views.penalty import *

urlpatterns = [
    path("penalties/", PenaltiesListView.as_view(), name="penalties"),
    path("penalty_status/", PenaltyStatusListView.as_view(), name="penalty_status"),
    path("penalty_charges/", PenaltyChargesListView.as_view(), name="penalty_charges"),
    path("penalty_status_types/", PenaltyStatusTypesListView.as_view(), name="penalty_status_types"),
]
