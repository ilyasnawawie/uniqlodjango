from .base import ItemListView
from evhome.models.penalty import Penalties


class PenaltiesListView(ItemListView):
    model = Penalties
    model_name = Penalties._meta.verbose_name_plural

    def get(self, request):
        self.message = f"Got {self.model_name}."
        return super().get(request)
