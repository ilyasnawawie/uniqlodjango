from .base import ItemListView
from evhome.models.chargepointport import ChargePointPortPrices

class ChargePointPortPricesListView(ItemListView):
    model = ChargePointPortPrices
    model_name = "charge point port prices"
    message = "Got charge point port prices."
