from django.contrib import admin

from .models import ApartPars, Booking


class ApartParsAdmin(admin.ModelAdmin):
    list_display = ('imageUrl', 'city', 'address', 'name', 'descriptions', 'price', 'priceNumber')
    search_fields = ('id', 'city', 'name')
    list_filter = ('city',)


admin.site.register(ApartPars, ApartParsAdmin)


class BookingAdmin(admin.ModelAdmin):
    list_display = ('city', 'checkInDate', 'checkOutDate', 'contactPerson', 'date', 'paid')


admin.site.register(Booking, BookingAdmin)
