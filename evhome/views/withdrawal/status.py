from evhome.models import WithdrawalStatus
from .base import ItemListView


class WithdrawalStatusListView(ItemListView):
    model = WithdrawalStatus
    model_name = WithdrawalStatus._meta.verbose_name_plural

    def get(self, request):
        self.message = f"Got {self.model_name}."
        return super().get(request)
