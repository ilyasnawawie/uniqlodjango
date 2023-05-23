from .base import ItemListView
from evhome.models.tokens import AuthTokens

class AuthTokensListView(ItemListView):
    model = AuthTokens
    model_name = 'tokens'
    message = 'Got tokens.'
