from .base import ItemListView
from evhome.models.chargepointport import ChargePointPortStatus


class ChargePointPortStatusListView(ItemListView):
    model = ChargePointPortStatus
    model_name = ChargePointPortStatus._meta.verbose_name_plural
    secondary_sort_column = 'timestamp'

    def get(self, request):
        self.message = f"Got {self.model_name}."
        return super().get(request)
