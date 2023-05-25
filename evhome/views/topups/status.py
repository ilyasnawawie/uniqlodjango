from evhome.models import TopUpStatus
from .base import ItemListView


class TopUpStatusListView(ItemListView):
    model = TopUpStatus
    model_name = TopUpStatus._meta.verbose_name_plural

    def get(self, request):
        self.message = f"Got {self.model_name}."
        return super().get(request)
