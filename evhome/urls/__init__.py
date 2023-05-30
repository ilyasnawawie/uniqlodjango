from .auth_urls import urlpatterns as auth_patterns
from .charge_point_locations_urls import urlpatterns as charge_point_locations_patterns
from .car_urls import urlpatterns as car_patterns
from .charge_point_port_urls import urlpatterns as charge_point_port_patterns
from .topups_urls import urlpatterns as top_ups_patterns
from .faults_urls import urlpatterns as faults_patterns

urlpatterns = (
    auth_patterns
    + charge_point_locations_patterns
    + car_patterns
    + charge_point_port_patterns
    + top_ups_patterns
    + faults_patterns
)
