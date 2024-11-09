from rest_framework import serializers
from .models import ApartPars, Booking


class ApartParsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApartPars
        fields = "__all__"


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
