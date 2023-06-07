from evhome.models import WithdrawalStatusType
from .base import ItemListView


class WithdrawalStatusTypeListView(ItemListView):
    model = WithdrawalStatusType
    model_name = WithdrawalStatusType._meta.verbose_name_plural
    secondary_sort_column = 'name'

    def get(self, request):
        self.message = f"Got {self.model_name}."
        return super().get(request)