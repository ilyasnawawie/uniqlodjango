from .base import ItemListView
from evhome.models.chargelocation import ChargePointLocations

class ChargePointLocationsListView(ItemListView):
    model = ChargePointLocations
    model_name = 'charge point locations'
    message = 'Got charge point locations.'
