from .base import ItemListView
from evhome.models.penalty import PenaltyCharges


class PenaltyChargesListView(ItemListView):
    model = PenaltyCharges
    model_name = PenaltyCharges._meta.verbose_name_plural

    def get(self, request):
        self.message = f"Got {self.model_name}."
        return super().get(request)
