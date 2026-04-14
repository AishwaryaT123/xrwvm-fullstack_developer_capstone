from django.db import models
from django.utils.timezone import now


class CarMake(models.Model):
    name = models.CharField(null=False, max_length=30, default='Car Make')
    description = models.CharField(max_length=200, default='Car Make Description')

    def __str__(self):
        return self.name


class CarModel(models.Model):
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('COUPE', 'Coupe'),
        ('TRUCK', 'Truck'),
    ]
    car_make = models.ForeignKey(CarMake, null=True, on_delete=models.CASCADE)
    dealer_id = models.IntegerField(null=True)
    name = models.CharField(null=False, max_length=30, default='Car Model')
    car_type = models.CharField(null=False, max_length=10, choices=CAR_TYPES, default='SUV')
    year = models.DateField(null=True)
    engine = models.CharField(null=True, max_length=50, default='V6')

    def __str__(self):
        return self.name


class CarDealer:
    def __init__(self, address, city, full_name, id, lat, long, short_name, st, zip):
        self.address = address
        self.city = city
        self.full_name = full_name
        self.id = id
        self.lat = lat
        self.long = long
        self.short_name = short_name
        self.st = st
        self.zip = zip

    def __str__(self):
        return "Dealer name: " + self.full_name


class DealerReview:
    def __init__(self, dealership, name, purchase, review, purchase_date, car_make,
                 car_model, car_year, sentiment, id):
        self.dealership = dealership
        self.name = name
        self.purchase = purchase
        self.review = review
        self.purchase_date = purchase_date
        self.car_make = car_make
        self.car_model = car_model
        self.car_year = car_year
        self.sentiment = sentiment
        self.id = id

    def __str__(self):
        return "Review: " + self.review
