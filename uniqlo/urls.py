from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('evhome/', include('evhome.urls')),
    # Add the URL pattern for the empty path
    path('', include('evhome.urls')),  # Replace 'evhome.urls' with the appropriate module name
]
