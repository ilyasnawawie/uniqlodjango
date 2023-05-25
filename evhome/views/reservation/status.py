from .base import ItemListView
from evhome.models.reservation import ReservationStatus


class ReservationsStatusListView(ItemListView):
    model = ReservationStatus
    model_name = ReservationStatus._meta.verbose_name_plural

    def get(self, request):
        self.message = f"Got {self.model_name}."
        return super().get(request)
