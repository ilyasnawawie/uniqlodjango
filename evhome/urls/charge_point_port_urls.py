from django.urls import path
from ..views.charge_point_port import *

urlpatterns = [
    path(
        "charge_point_port/",
        ChargePointPortListView.as_view(),
        name="charge_point_port",
    ),
    path(
        "charge_point_port_error_code_types/",
        ChargePointPortErrorCodeTypesListView.as_view(),
        name="charge_point_port_error_code_types",
    ),
    path(
        "meter_values/",
        ChargePointPortMeterValuesListView.as_view(),
        name="charge_point_port_meter_values",
    ),
    path(
        "prices/",
        ChargePointPortPricesListView.as_view(),
        name="charge_point_port_prices",
    ),
    path(
        "status/",
        ChargePointPortStatusListView.as_view(),
        name="charge_point_port_status",
    ),
    path(
        "status_types/",
        ChargePointPortStatusTypesListView.as_view(),
        name="charge_point_port_status_types",
    ),
]
