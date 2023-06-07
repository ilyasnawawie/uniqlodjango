from .base import ItemListView
from evhome.models.penalty import PenaltyStatus


class PenaltyStatusListView(ItemListView):
    model = PenaltyStatus
    model_name = PenaltyStatus._meta.verbose_name_plural
    secondary_sort_column = 'amount'

    def get(self, request):
        self.message = f"Got {self.model_name}."
        return super().get(request)
