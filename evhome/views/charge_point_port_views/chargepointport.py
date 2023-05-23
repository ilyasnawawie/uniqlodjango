from .base import ItemListView
from evhome.models.chargepointport import ChargePointPort

class ChargePointPortListView(ItemListView):
    model = ChargePointPort
    model_name = "charge port point"
    message = "Got charge point port."
