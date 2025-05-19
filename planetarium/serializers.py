from rest_framework import serializers
from planetarium.models import (
    User,
    Reservation,
    PlanetariumDome,
    ShowTheme,
    AstronomyShow,
    ShowSession,
    Ticket
)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "first_name", "last_name")


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ("id", "created_at", "user")


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
