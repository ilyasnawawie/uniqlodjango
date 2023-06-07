from evhome.models import TopUpType
from .base import ItemListView


class TopUpTypeListView(ItemListView):
    model = TopUpType
    model_name = TopUpType._meta.verbose_name_plural
    secondary_sort_column = 'name'

    def get(self, request):
        self.message = f"Got {self.model_name}."
        return super().get(request)
