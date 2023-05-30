from django.urls import path
from ..views.fault import *

urlpatterns = [
    path("faults/", FaultsListView.as_view(), name="faults"),
    path("fault_types/", FaultTypesListView.as_view(), name="fault_types"),
]
