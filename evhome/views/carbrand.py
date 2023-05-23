from .base import ItemListView
from evhome.models.carbrand_model import CarBrand


class CarBrandListView(ItemListView):
    model = CarBrand
    model_name = "car brand"
    message = "Got car brand."
