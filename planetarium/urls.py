from django.urls import path, include
from rest_framework.routers import DefaultRouter
from planetarium.schemas import (
    ShowThemeViewSet,
    AstronomyShowViewSet,
    PlanetariumDomeViewSet,
    ReservationViewSet,
    ShowSessionViewSet,
    # TicketViewSet,
)

app_name = "planetarium"

router = DefaultRouter()
router.register(
    "show-themes",
    ShowThemeViewSet,
    basename="show-theme"
)
router.register(
    "astronomy-shows",
    AstronomyShowViewSet,
    basename="astronomy-show"
)
router.register(
    "planetarium-domes",
    PlanetariumDomeViewSet,
    basename="planetarium-dome"
)
router.register(
    "reservations",
    ReservationViewSet,
    basename="reservation"
)
router.register(
    "show-sessions",
    ShowSessionViewSet,
    basename="show-session"
)
# router.register(
#     "tickets",
#     TicketViewSet,
#     basename="ticket"
# )

urlpatterns = [
    path("", include(router.urls)),
]