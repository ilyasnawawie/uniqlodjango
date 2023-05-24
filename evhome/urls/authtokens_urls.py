from django.urls import path
from ..views import AuthTokensListView

urlpatterns = [
    path('auth_tokens/', AuthTokensListView.as_view(), name='auth_tokens'),
]
