from django.db import models
import datetime


# Create your models here.
class ApartPars(models.Model):
    id = models.AutoField(primary_key=True)
    imageUrl = models.URLField(max_length=200, null=True)
    city = models.CharField(max_length=100, null=True, verbose_name="Город")
    address = models.CharField(max_length=100, null=True, verbose_name="Адрес")
    name = models.CharField(max_length=100, null=True, verbose_name="Название аппартаментов")
    descriptions = models.TextField(null=True, blank=True, verbose_name='Описание апартаментов')
    price = models.CharField(max_length=100, verbose_name="Цена проживания за сутки (текст)")
    priceNumber = models.DecimalField(verbose_name='Цена проживания за сутки (число)', decimal_places=0, max_digits=10, default=0)

    def __str__(self):
        return (f'{self.name}')


class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    city = models.ForeignKey(ApartPars, on_delete=models.CASCADE)
    checkInDate = models.DateField(default=datetime.date.today)
    checkOutDate = models.DateField(default=datetime.date.today)
    contactPerson = models.CharField(max_length=150, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return (f'{self.contactPerson}')
