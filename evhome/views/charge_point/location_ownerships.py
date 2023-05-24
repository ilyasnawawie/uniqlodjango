from .base import ItemListView
from evhome.models.chargelocation import ChargePointLocationOwnerships


class ChargePointLocationsOwnershipsListView(ItemListView):
    model = ChargePointLocationOwnerships
    model_name = "charge point locations ownerships"
    message = "Got charge point locations ownerships."
