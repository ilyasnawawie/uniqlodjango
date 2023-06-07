from .base import ItemListView
from evhome.models.chargepointport import ChargePointPortPrices


class ChargePointPortPricesListView(ItemListView):
    model = ChargePointPortPrices
    model_name = ChargePointPortPrices._meta.verbose_name_plural
    secondary_sort_column = 'price'

    def get(self, request):
        self.message = f"Got {self.model_name}."
        return super().get(request)
