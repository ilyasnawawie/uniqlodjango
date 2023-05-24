from .base import ItemListView
from evhome.models.authuser import AuthUser

class AuthUserListView(ItemListView):
    model = AuthUser
    model_name = AuthUser._meta.verbose_name_plural

    def get(self, request):
        self.message = f"Got {self.model_name}."
        return super().get(request)
