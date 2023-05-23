from .base import ItemListView
from evhome.models.authuser import AuthUser

class AuthUserListView(ItemListView):
    model = AuthUser
    model_name = 'auth user'
    message = 'Got auth user.'
