from django.urls import path
from ..views import AuthUserListView

urlpatterns = [
    path('', AuthUserListView.as_view(), name='auth_user'),
]
