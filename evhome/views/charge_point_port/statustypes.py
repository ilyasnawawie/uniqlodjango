from .base import ItemListView
from evhome.models.chargepointport import ChargePointPortStatusTypes


class ChargePointPortStatusTypesListView(ItemListView):
    model = ChargePointPortStatusTypes
    model_name = ChargePointPortStatusTypes._meta.verbose_name_plural
    secondary_sort_column = 'name'

    def get(self, request):
        self.message = f"Got {self.model_name}."
        return super().get(request)
