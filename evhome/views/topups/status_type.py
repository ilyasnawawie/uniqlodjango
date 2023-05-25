from evhome.models import TopUpStatusType
from .base import ItemListView


class TopUpStatusTypeListView(ItemListView):
    model = TopUpStatusType
    model_name = TopUpStatusType._meta.verbose_name_plural

    def get(self, request):
        self.message = f"Got {self.model_name}."
        return super().get(request)
