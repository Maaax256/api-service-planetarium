from django.contrib import admin

from planetarium.models import (
    AstronomyShow,
    ShowTheme,
    Reservation,
    PlanetariumDome,
    ShowSession,
    Ticket
)


admin.site.register(ShowTheme)
admin.site.register(AstronomyShow)
admin.site.register(Reservation)
admin.site.register(PlanetariumDome)
admin.site.register(ShowSession)
admin.site.register(Ticket)
