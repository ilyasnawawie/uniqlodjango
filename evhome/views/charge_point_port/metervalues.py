from .base import ItemListView
from evhome.models.chargepointport import ChargePointPortMeterValues


class ChargePointPortMeterValuesListView(ItemListView):
    model = ChargePointPortMeterValues
    model_name = ChargePointPortMeterValues._meta.verbose_name_plural

    def get(self, request):
        self.message = f"Got {self.model_name}."
        return super().get(request)
