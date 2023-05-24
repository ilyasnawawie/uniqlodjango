from .adminauthtokens_urls import urlpatterns as adminauthtokens_patterns
from .authgroups_urls import urlpatterns as authgroups_patterns
from .authtokens_urls import urlpatterns as authtokens_patterns
from .authuser_urls import urlpatterns as authuser_patterns
from .chargepointlocations_urls import urlpatterns as chargepointlocations_patterns
from .carbrand_urls import urlpatterns as carbrand_patterns
from .carmodel_urls import urlpatterns as carmodel_patterns
from .charge_point_port_urls import urlpatterns as chargepointport_patterns

urlpatterns = (
    adminauthtokens_patterns +
    authgroups_patterns +
    authtokens_patterns +
    authuser_patterns +
    chargepointlocations_patterns +
    carbrand_patterns +
    carmodel_patterns +
    chargepointport_patterns
)
