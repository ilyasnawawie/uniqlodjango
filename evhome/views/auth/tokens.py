from .base import ItemListView
from evhome.models.tokens import AuthTokens


class AuthTokensListView(ItemListView):
    model = AuthTokens
    model_name = AuthTokens._meta.verbose_name_plural

    def get(self, request):
        self.message = f"Got {self.model_name}."
        return super().get(request)
