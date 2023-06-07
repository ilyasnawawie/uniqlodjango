from .base import ItemListView
from evhome.models.orders import Orders


class OrdersListView(ItemListView):
    model = Orders
    model_name = Orders._meta.verbose_name_plural
    secondary_sort_column = 'order_no'

    def get(self, request):
        self.message = f"Got {self.model_name}."
        return super().get(request)
