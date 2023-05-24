from django.urls import path
from ..views import AdminAuthTokensListView

urlpatterns = [
    path('admin_auth_tokens/', AdminAuthTokensListView.as_view(), name='admin_auth_tokens'),
]
