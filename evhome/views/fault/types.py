from .base import ItemListView
from evhome.models.faults import FaultTypes


class FaultTypesListView(ItemListView):
    model = FaultTypes
    model_name = FaultTypes._meta.verbose_name_plural

    def get(self, request):
        self.message = f"Got {self.model_name}."
        return super().get(request)
