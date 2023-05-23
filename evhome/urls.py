from django.urls import path
from .views import admin_auth_tokens

app_name = 'evhome'

urlpatterns = [
    path('admin_auth_tokens/', admin_auth_tokens, name='admin_auth_tokens'),
    # ...
]
