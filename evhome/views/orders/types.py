from .base import ItemListView
from evhome.models.orders import OrderTypes


class OrderTypesListView(ItemListView):
    model = OrderTypes
    model_name = OrderTypes._meta.verbose_name_plural

    def get(self, request):
        self.message = f"Got {self.model_name}."
        return super().get(request)
