from .base import ItemListView
from evhome.models.orders import OrderStatusReasonTypes


class OrderStatusReasonTypesListView(ItemListView):
    model = OrderStatusReasonTypes
    model_name = OrderStatusReasonTypes._meta.verbose_name_plural

    def get(self, request):
        self.message = f"Got {self.model_name}."
        return super().get(request)
