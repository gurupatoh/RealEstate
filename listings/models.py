from django.db import models
from django.utils.timezone import now
from realtors.models import Realtors


class Listing(models.Model):
    class SaleType(models.TextChoices):
        FOR_SALE = 'for sale '
        FOR_RENT = 'for rent '

    class HomeType(models.TextChoices):
        APARTMENTS = 'apartment'
        BEDSITTERS = 'bedsitter'
        COMMERCIAL_PROPERTIES = 'commercialProperties'
        HOUSES = ' house '
        SINGLES = 'single'
        BEDROOM = ' bedroom'
        LAND = 'land'

    realtor = models.ForeignKey(Realtors, on_delete=models.DO_NOTHING)
    slug = models.SlugField(max_length=200, unique=True)
    title = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    county = models.CharField(max_length=150)
    town = models.CharField(max_length=150)
    description = models.TextField(max_length=250, blank=True)
    sale_type = models.CharField(max_length=50, choices=SaleType.choices, default=SaleType.FOR_SALE)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    home_type = models.CharField(max_length=50, choices=HomeType.choices, default=HomeType.BEDSITTERS)
    square_foot = models.IntegerField()
    open_house = models.BooleanField(default=False)
    photo_main = models.ImageField(upload_to='photos/%Y%m%d/', blank=True)
    photo_1 = models.ImageField(upload_to='photos/%Y%m%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y%m%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y%m%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y%m%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=now, blank=True)

    def __str__(self):
        return self.title
