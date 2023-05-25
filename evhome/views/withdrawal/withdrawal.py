from evhome.models import Withdrawal
from .base import ItemListView


class WithdrawalListView(ItemListView):
    model = Withdrawal
    model_name = Withdrawal._meta.verbose_name_plural

    def get(self, request):
        self.message = f"Got {self.model_name}."
        return super().get(request)
