from .base import ItemListView
from evhome.models.chargepointport import ChargePointPortMeterValues

class ChargePointPortMeterValuesListView(ItemListView):
    model = ChargePointPortMeterValues
    model_name = "charge point port meter values"
    message = "Got charge point port meter values."
