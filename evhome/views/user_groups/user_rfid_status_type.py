from evhome.models import UserGroupUserRfidStatusType
from .base import ItemListView


class UserGroupUserRfidStatusTypeListView(ItemListView):
    model = UserGroupUserRfidStatusType
    model_name = UserGroupUserRfidStatusType._meta.verbose_name_plural

    def get(self, request):
        self.message = f"Got {self.model_name}."
        return super().get(request)
