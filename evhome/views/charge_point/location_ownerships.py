from .base import ItemListView
from evhome.models.chargelocation import ChargePointLocationOwnerships


class ChargePointLocationsOwnershipsListView(ItemListView):
    model = ChargePointLocationOwnerships
    model_name = ChargePointLocationOwnerships._meta.verbose_name_plural

    def get(self, request):
        self.message = f"Got {self.model_name}."
        return super().get(request)
