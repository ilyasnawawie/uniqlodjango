from .base import ItemListView
from evhome.models.chargepointport import ChargePointPortStatus

class ChargePointPortStatusListView(ItemListView):
    model = ChargePointPortStatus
    model_name = "charge point port status"
    message = "Got charge point port status."
