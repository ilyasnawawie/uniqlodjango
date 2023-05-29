from django.urls import path
from ..views.user_groups import *

urlpatterns = [
    path("user_group_users/", UserGroupUserListView(), name="user_group_users"),
    path("user_groups/", UserGroupListView.as_view(), name="user_groups"),
    path("user/", UserListView.as_view(), name="user"),
    path("user_group_user_rfid/", UserGroupUserRfidListView.as_view(), name="top_up_type"),
]