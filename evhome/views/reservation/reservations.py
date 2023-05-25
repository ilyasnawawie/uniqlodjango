from .base import ItemListView
from evhome.models.reservation import Reservations


class ReservationsListView(ItemListView):
    model = Reservations
    model_name = Reservations._meta.verbose_name_plural

    def get(self, request):
        self.message = f"Got {self.model_name}."
        return super().get(request)
