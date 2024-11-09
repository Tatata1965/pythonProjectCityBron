from .models import ApartPars, Booking
from rest_framework import viewsets, permissions
from .serializers import ApartParsSerializer, BookingSerializer


class ApartParsViewSet(viewsets.ModelViewSet):
    queryset = ApartPars.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ApartParsSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = BookingSerializer
