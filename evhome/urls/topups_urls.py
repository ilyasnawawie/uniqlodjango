from django.urls import path
from ..views.topups import TopUpListView, TopUpStatusTypeListView, TopUpStatusListView, TopUpTypeListView

urlpatterns = [
    path("topup/", TopUpListView.as_view(), name="top_up"),
    path("topup_status/", TopUpStatusListView.as_view(), name="top_up_status"),
    path("topup_status_type/", TopUpStatusTypeListView.as_view(), name="top_up_status_type"),
    path("topup_type/", TopUpTypeListView.as_view(), name="top_up_type"),
]
