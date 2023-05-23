from .base import ItemListView
from evhome.models.authgroups import AuthGroup

class AuthGroupListView(ItemListView):
    model = AuthGroup
    model_name = 'auth groups'
    message = 'Got auth groups.'
