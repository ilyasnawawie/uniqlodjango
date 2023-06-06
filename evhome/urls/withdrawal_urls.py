from django.urls import path
from ..views.withdrawal import *

urlpatterns = [
    path("withdrawal/", WithdrawalListView.as_view(), name="withdrawal"),
    path("withdrawal_status/", WithdrawalTypeListView.as_view(), name="withdrawal_status"),
    path("withdrawal_status/", WithdrawalStatusListView.as_view(), name="withdrawal_status"),
    path("withdrawal_status_type/", WithdrawalStatusTypeListView.as_view(), name="withdrawal_status_type")
]