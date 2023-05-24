from .base import ItemListView
from evhome.models.authgroups import AuthGroup

class AuthGroupListView(ItemListView):
    model = AuthGroup
    model_name = AuthGroup._meta.verbose_name_plural

    def get(self, request):
        self.message = f"Got {self.model_name}."
        return super().get(request)
