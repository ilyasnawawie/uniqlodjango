from .base import ItemListView
from evhome.models.carbrand_model import UserCar


class UserCarListView(ItemListView):
    model = UserCar
    model_name = UserCar._meta.verbose_name_plural
    secondary_sort_column = 'car_model'

    def get(self, request):
        self.message = f"Got {self.model_name}."
        return super().get(request)
