from .base import ItemListView
from evhome.models.faults import Faults


class FaultsListView(ItemListView):
    model = Faults
    model_name = Faults._meta.verbose_name_plural

    def get(self, request):
        self.message = f"Got {self.model_name}."
        return super().get(request)
