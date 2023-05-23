from django.urls import path
from ..views import AuthTokensListView

urlpatterns = [
    path('', AuthTokensListView.as_view(), name='auth_tokens'),
]
