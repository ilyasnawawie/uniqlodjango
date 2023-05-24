from .base import ItemListView
from evhome.models.chargepointport import ChargePointPortErrorCodeTypes


class ChargePointPortErrorCodeTypesListView(ItemListView):
    model = ChargePointPortErrorCodeTypes
    model_name = "charge point port error code types"
    message = "Got charge point port error code types."
