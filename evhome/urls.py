from django.urls import path
from .views import items_list

app_name = 'evhome'

urlpatterns = [
    path('admin_auth_tokens/', items_list, name='admin_auth_tokens'),
    path('auth_tokens/', items_list, name='auth_tokens'),
    path('charge_point_locations/', items_list, name='charge_point_locations'),
    path('auth_groups/', items_list, name='auth_groups'),
    path('auth_user/', items_list, name='auth_user'),
    # ...
]
