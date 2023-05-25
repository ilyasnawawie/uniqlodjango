from evhome.models import WithdrawalType
from .base import ItemListView


class WithdrawalTypeListView(ItemListView):
    model = WithdrawalType
    model_name = WithdrawalType._meta.verbose_name_plural

    def get(self, request):
        self.message = f"Got {self.model_name}."
        return super().get(request)
