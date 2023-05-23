from django.urls import path
from ..views import AuthGroupListView

urlpatterns = [
    path('', AuthGroupListView.as_view(), name='auth_groups'),
]
