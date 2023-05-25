from evhome.models import UserGroup
from .base import ItemListView


class UserGroupListView(ItemListView):
    model = UserGroup
    model_name = UserGroup._meta.verbose_name_plural

    def get(self, request):
        self.message = f"Got {self.model_name}."
        return super().get(request)
