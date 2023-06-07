from .base import ItemListView
from evhome.models.chargelocation import ChargePointLocations


class ChargePointLocationsListView(ItemListView):
    model = ChargePointLocations
    model_name = ChargePointLocations._meta.verbose_name_plural
    secondary_sort_column = 'name'

    def get(self, request):
        self.message = f"Got {self.model_name}."
        return super().get(request)
