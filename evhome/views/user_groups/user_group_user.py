from evhome.models import UserGroupUser
from .base import ItemListView


class UserGroupUserListView(ItemListView):
    model = UserGroupUser
    model_name = UserGroupUser._meta.verbose_name_plural

    def get(self, request):
        self.message = f"Got {self.model_name}."
        return super().get(request)
