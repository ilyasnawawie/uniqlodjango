from .base import ItemListView
from evhome.models.reservation import ReservationStatusTypes


class ReservationsStatusTypesListView(ItemListView):
    model = ReservationStatusTypes
    model_name = ReservationStatusTypes._meta.verbose_name_plural

    def get(self, request):
        self.message = f"Got {self.model_name}."
        return super().get(request)
