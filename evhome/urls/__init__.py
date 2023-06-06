from .auth_urls import urlpatterns as auth_patterns
from .charge_point_locations_urls import urlpatterns as charge_point_locations_patterns
from .car_urls import urlpatterns as car_patterns
from .charge_point_port_urls import urlpatterns as charge_point_port_patterns
from .topups_urls import urlpatterns as top_ups_patterns
from .faults_urls import urlpatterns as faults_patterns
from .penalty_urls import urlpatterns as penalty_patterns
from .orders_urls import urlpatterns as orders_patterns
from .reservation_urls import urlpatterns as reservation_patterns
from .wallets_urls import urlpatterns as wallet_patterns
from .withdrawal_urls import urlpatterns as withdrawal_patterns

urlpatterns = (
    auth_patterns
    + charge_point_locations_patterns
    + car_patterns
    + charge_point_port_patterns
    + top_ups_patterns
    + faults_patterns
    + penalty_patterns
    + orders_patterns
    + reservation_patterns
    + wallet_patterns
    + withdrawal_patterns
)
