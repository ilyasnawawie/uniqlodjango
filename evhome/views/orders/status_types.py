from .base import ItemListView
from evhome.models.orders import OrderStatusTypes


class OrderStatusTypesListView(ItemListView):
    model = OrderStatusTypes
    model_name = OrderStatusTypes._meta.verbose_name_plural
    secondary_sort_column = 'name'

    def get(self, request):
        self.message = f"Got {self.model_name}."
        return super().get(request)
