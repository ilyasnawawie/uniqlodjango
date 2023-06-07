from evhome.models import Wallet
from .base import ItemListView


class WalletListView(ItemListView):
    model = Wallet
    model_name = Wallet._meta.verbose_name_plural
    secondary_sort_column = 'balance'

    def get(self, request):
        self.message = f"Got {self.model_name}."
        return super().get(request)
