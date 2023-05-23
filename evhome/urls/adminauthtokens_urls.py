from django.urls import path
from ..views import AdminAuthTokensListView

urlpatterns = [
    path('', AdminAuthTokensListView.as_view(), name='admin_auth_tokens'),
]
