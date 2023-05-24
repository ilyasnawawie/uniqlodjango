from django.urls import path
from ..views import AuthGroupListView

urlpatterns = [
    path('auth_groups/', AuthGroupListView.as_view(), name='auth_groups'),
]
