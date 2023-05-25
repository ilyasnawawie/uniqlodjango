from evhome.models import UserGroupUserRfid
from .base import ItemListView


class UserGroupUserRfidListView(ItemListView):
    model = UserGroupUserRfid
    model_name = UserGroupUserRfid._meta.verbose_name_plural

    def get(self, request):
        self.message = f"Got {self.model_name}."
        return super().get(request)
