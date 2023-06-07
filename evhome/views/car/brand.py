from .base import ItemListView
from evhome.models.carbrand_model import CarBrand


class CarBrandListView(ItemListView):
    model = CarBrand
    model_name = CarBrand._meta.verbose_name_plural
    secondary_sort_column = 'carmodel'

    def get(self, request):
        self.message = f"Got {self.model_name}."
        return super().get(request)
