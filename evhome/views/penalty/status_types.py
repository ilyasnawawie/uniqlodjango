from .base import ItemListView
from evhome.models.penalty import PenaltyStatusTypes


class PenaltyStatusTypesListView(ItemListView):
    model = PenaltyStatusTypes
    model_name = PenaltyStatusTypes._meta.verbose_name_plural

    def get(self, request):
        self.message = f"Got {self.model_name}."
        return super().get(request)
