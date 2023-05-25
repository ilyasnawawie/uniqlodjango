from .base import ItemListView
from evhome.models.orders import OrderStatus


class OrderStatusListView(ItemListView):
    model = OrderStatus
    model_name = OrderStatus._meta.verbose_name_plural

    def get(self, request):
        self.message = f"Got {self.model_name}."
        return super().get(request)
