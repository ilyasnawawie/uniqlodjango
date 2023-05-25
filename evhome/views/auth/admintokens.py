from .base import ItemListView
from evhome.models.tokens import AdminAuthTokens


class AdminAuthTokensListView(ItemListView):
    model = AdminAuthTokens
    model_name = AdminAuthTokens._meta.verbose_name_plural

    def get(self, request):
        self.message = f"Got {self.model._meta.verbose_name_plural}."
        return super().get(request)
