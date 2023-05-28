from evhome.models import Users
from .base import ItemListView


class UsersListView(ItemListView):
    model = Users
    model_name = "users"  # Assign string directly

    def get(self, request):
        self.message = f"Got {self.model_name}."
        return super().get(request)

