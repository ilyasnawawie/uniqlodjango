from .auth_urls import urlpatterns as auth_patterns
from .charge_point_locations_urls import urlpatterns as chargepointlocations_patterns
from .car_urls import urlpatterns as car_patterns
from .charge_point_port_urls import urlpatterns as chargepointport_patterns

urlpatterns = (
    auth_patterns
    + chargepointlocations_patterns
    + car_patterns
    + chargepointport_patterns
)
