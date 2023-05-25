from .base import ItemListView
from evhome.models.chargepointport import ChargePointPortErrorCodeTypes


class ChargePointPortErrorCodeTypesListView(ItemListView):
    model = ChargePointPortErrorCodeTypes
    model_name = ChargePointPortErrorCodeTypes._meta.verbose_name_plural

    def get(self, request):
        self.message = f"Got {self.model_name}."
        return super().get(request)
