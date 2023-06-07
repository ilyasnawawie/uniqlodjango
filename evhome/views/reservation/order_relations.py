from .base import ItemListView
from evhome.models.reservation import ReservationOrderRelations


class ReservationsOrderRelationsListView(ItemListView):
    model = ReservationOrderRelations
    model_name = ReservationOrderRelations._meta.verbose_name_plural
    secondary_sort_column = 'order'
    def get(self, request):
        self.message = f"Got {self.model_name}."
        return super().get(request)
