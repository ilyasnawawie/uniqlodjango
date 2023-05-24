from .base import ItemListView
from evhome.models.carbrand_model import CarModel

class CarModelListView(ItemListView):
    model = CarModel
    model_name = "car model"
    message = "Got car model."
