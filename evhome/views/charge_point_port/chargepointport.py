from .base import ItemListView
from evhome.models.chargepointport import ChargePointPort


class ChargePointPortListView(ItemListView):
    model = ChargePointPort
    model_name = ChargePointPort._meta.verbose_name_plural
    secondary_sort_column = 'power'
    def get(self, request):
        self.message = f"Got {self.model_name}."
        return super().get(request)
