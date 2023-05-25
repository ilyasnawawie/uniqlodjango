from evhome.models import TopUp
from .base import ItemListView


class TopUpListView(ItemListView):
    model = TopUp
    model_name = TopUp._meta.verbose_name_plural

    def get(self, request):
        self.message = f"Got {self.model_name}."
        return super().get(request)
