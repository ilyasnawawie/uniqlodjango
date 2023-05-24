from .base import ItemListView
from evhome.models.chargepointport import ChargePointPortStatusTypes


class ChargePointPortStatusTypesListView(ItemListView):
    model = ChargePointPortStatusTypes
    model_name = "charge point port status types"
    message = "Got charge point port status types."
