from django.urls import path
from ..views import AuthUserListView

urlpatterns = [
    path('auth_user/', AuthUserListView.as_view(), name='auth_user'),
]
