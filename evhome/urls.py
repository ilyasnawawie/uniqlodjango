from django.urls import path
from .views import (
    AdminAuthTokensListView,
    AuthGroupListView,
    AuthTokensListView,
    AuthUserListView,
    ChargePointLocationsListView,
    ChargePointLocationsOwnershipsListView,
    CarBrandListView,
    CarModelListView,
)

urlpatterns = [
    path(
        "admin_auth_tokens/",
        AdminAuthTokensListView.as_view(),
        name="admin_auth_tokens",
    ),
    path("auth_groups/", AuthGroupListView.as_view(), name="auth_groups"),
    path("auth_tokens/", AuthTokensListView.as_view(), name="auth_tokens"),
    path("auth_user/", AuthUserListView.as_view(), name="auth_user"),
    path(
        "charge_point_locations/",
        ChargePointLocationsListView.as_view(),
        name="charge_point_locations",
    ),
    path(
        "charge_point_location_ownerships/",
        ChargePointLocationsOwnershipsListView.as_view(),
        name="charge_location_ownerships",
    ),
    path("car_brand/", CarBrandListView.as_view(), name="car_brand"),
    path("car_model/", CarModelListView.as_view(), name="car_model"),
]
