from .base import ItemListView
from evhome.models.tokens import AdminAuthTokens


class AdminAuthTokensListView(ItemListView):
    model = AdminAuthTokens
    model_name = "admin tokens"
    message = "Got admin tokens."
