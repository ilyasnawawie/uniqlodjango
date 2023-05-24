from .base import ItemListView
from evhome.models.chargelocation import ChargePoints

class ChargePointListView(ItemListView):
    model = ChargePoints
    model_name = "charge point"
    message = "Got charge point."
