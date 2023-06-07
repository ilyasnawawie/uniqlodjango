from .base import ItemListView
from evhome.models.carbrand_model import CarModel


class CarModelListView(ItemListView):
    model = CarModel
    model_name = CarModel._meta.verbose_name_plural
    secondary_sort_column = 'year'
    def get(self, request):
        self.message = f"Got {self.model_name}."
        return super().get(request)
