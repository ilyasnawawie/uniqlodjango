from django.urls import path
from ..views.orders import *

urlpatterns = [
    path("orders/", OrdersListView.as_view(), name="orders"),
    path("order_status/", OrderStatusListView.as_view(), name="order_status"),
    path("order_types/", OrderTypesListView.as_view(), name="order_types"),
    path("order_status_types/", OrderStatusTypesListView.as_view(), name="order_status_types"),
    path("order_status_reason_types/", OrderStatusReasonTypesListView.as_view(), name="order_status_reason_types"),
]
