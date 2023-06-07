from evhome.models import WalletTransactionType
from .base import ItemListView


class WalletTransactionTypeListView(ItemListView):
    model = WalletTransactionType
    model_name = WalletTransactionType._meta.verbose_name_plural
    secondary_sort_column = 'name'

    def get(self, request):
        self.message = f"Got {self.model_name}."
        return super().get(request)