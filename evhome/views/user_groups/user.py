from evhome.models import User
from .base import ItemListView


class UserListView(ItemListView):
    model = User
    model_name = User._meta.verbose_name_plural

    def get(self, request):
        self.message = f"Got {self.model_name}."
        return super().get(request)
