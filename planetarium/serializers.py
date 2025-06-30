from rest_framework import serializers
from planetarium.models import (
    Reservation,
    PlanetariumDome,
    ShowTheme,
    AstronomyShow,
    ShowSession,
    Ticket
)


class ReservationSerializer(serializers.ModelSerializer):
    ticket_ids = serializers.ListField(
        child=serializers.IntegerField(), write_only=True
    )

    class Meta:
        model = Reservation
        fields = ("id", "created_at", "user", "ticket_ids")
        read_only_fields = ("id", "created_at", "user")

    def create(self, validated_data):
        ticket_ids = validated_data.pop("ticket_ids")
        user = self.context["request"].user
        reservation = Reservation.objects.create(user=user)
        Ticket.objects.filter(
            id__in=ticket_ids,
            reservation__isnull=True
        ).update(reservation=reservation)
        return reservation


class PlanetariumDomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanetariumDome
        fields = ("id", "name", "rows", "seats_in_row")


class ShowThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowTheme
        fields = ("id", "name")


class AstronomyShowSerializer(serializers.ModelSerializer):
    show_themes = ShowThemeSerializer(many=True)

    class Meta:
        model = AstronomyShow
        fields = ("id", "title", "description", "show_themes")


class ShowSessionSerializer(serializers.ModelSerializer):
    astronomy_show = AstronomyShowSerializer()
    planetarium_dome = PlanetariumDomeSerializer()

    class Meta:
        model = ShowSession
        fields = ("id", "astronomy_show", "planetarium_dome", "show_time")


class TicketSerializer(serializers.ModelSerializer):
    show_session = ShowSessionSerializer()
    reservation = ReservationSerializer()

    class Meta:
        model = Ticket
        fields = ("id", "row", "seat", "show_session", "reservation")
