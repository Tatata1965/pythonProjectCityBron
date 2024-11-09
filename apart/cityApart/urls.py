from os import path

from rest_framework import routers
from .api import ApartParsViewSet, BookingViewSet

router = routers.DefaultRouter()

router.register('api/apartPars', ApartParsViewSet, 'apartPars')
router.register('api/booking', BookingViewSet, 'booking')
urlpatterns = router.urls



# urlpatterns = [
#     path('api/', ApartParsViewSet.as_view(), name='apartPars'),
# ]
