from .base import ItemListView
from evhome.models.chargelocation import ChargePoints


class ChargePointListView(ItemListView):
    model = ChargePoints
    model_name = ChargePoints._meta.verbose_name_plural
    secondary_sort_column = 'serial_number'
    display_fields = ['name', 'description', 'serial_number', 'model', 'vendor', 'firmware_version', 'iccid', 'imsi', 'meter_serial_number', 'meter_type']

    def get(self, request):
        self.message = f"Got {self.model_name}."
        return super().get(request)