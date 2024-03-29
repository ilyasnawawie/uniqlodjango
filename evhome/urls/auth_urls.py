from django.urls import path
from ..views.auth import *
from ..views.users import *

urlpatterns = [
    path(
        "admin_auth_tokens/",
        AdminAuthTokensListView.as_view(),
        name="admin_auth_tokens",
    ),
    path("auth_groups/", AuthGroupListView.as_view(), name="auth_groups"),
    path("auth_tokens/", AuthTokensListView.as_view(), name="auth_tokens"),
    path("auth_user/", AuthUserListView.as_view(), name="auth_user"),
    path("users/", UsersListView.as_view(), name="users"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),

]
