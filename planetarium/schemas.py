from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiParameter
from rest_framework import status

from planetarium.serializers import ShowThemeSerializer
from planetarium.views import (
    ShowThemeViewSet,
    AstronomyShowViewSet,
    PlanetariumDomeViewSet,
    ReservationViewSet,
    ShowSessionViewSet,
    # TicketViewSet,
)


ShowThemeViewSet = extend_schema_view(
    list=extend_schema(
        summary="List all show themes",
        description="Retrieve a list of all available show themes.",
        parameters=[
            OpenApiParameter(
                name="name",
                description="Filter by name",
                required=False,
                type=OpenApiTypes.STR,
            ),
        ],
    ),
    create=extend_schema(
        summary="Create a new show theme",
        description="Add a new show theme to the database.",
    ),
)(ShowThemeViewSet)


AstronomyShowViewSet = extend_schema_view(
    list=extend_schema(
        summary="List all astronomy shows",
        description="Retrieve a list of all available astronomy shows.",
    ),
    create=extend_schema(
        summary="Create a new astronomy show",
        description="Add a new astronomy show to the database.",
    ),
    retrieve=extend_schema(
        summary="Retrieve an astronomy show",
        description="Get details of a specific astronomy show by ID.",
    ),
)(AstronomyShowViewSet)


PlanetariumDomeViewSet = extend_schema_view(
    list=extend_schema(
        summary="List all planetarium domes",
        description="Retrieve a list of all available planetarium domes.",
    ),
    create=extend_schema(
        summary="Create a new planetarium dome",
        description="Add a new planetarium dome to the database.",
    ),
)(PlanetariumDomeViewSet)


ReservationViewSet = extend_schema_view(
    list=extend_schema(
        summary="List all reservations",
        description="Retrieve a list of all reservations.",
    ),
    create=extend_schema(
        summary="Create a new reservation",
        description="Add a new reservation to the database.",
    ),
)(ReservationViewSet)


ShowSessionViewSet = extend_schema_view(
    list=extend_schema(
        summary="List all show sessions",
        description="Retrieve a list of all available show sessions.",
    ),
    create=extend_schema(
        summary="Create a new show session",
        description="Add a new show session to the database.",
    ),
    retrieve=extend_schema(
        summary="Retrieve a show session",
        description="Get details of a specific show session by ID.",
    ),
)(ShowSessionViewSet)


# TicketViewSet = extend_schema_view(
#     list=extend_schema(
#         summary="List all tickets",
#         description="Retrieve a list of all tickets.",
#     ),
#     create=extend_schema(
#         summary="Create a new ticket",
#         description="Add a new ticket to the database.",
#     ),
# )(TicketViewSet)