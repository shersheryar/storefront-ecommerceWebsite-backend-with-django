from django.db import models

# Create your models here


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)


class Customer(models.Model):
    MEMEBERSHIP_BRONZE = 'B'
    MEMEBERSHIP_SILVER = 'S'
    MEMEBERSHIP_GOLD = 'G'

    MEMEBERSHIP_CHOICES = [
        (MEMEBERSHIP_BRONZE, 'Bronze'),
        (MEMEBERSHIP_SILVER, 'Silver'),
        (MEMEBERSHIP_GOLD, 'Gold'),
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    birth_date = models.DateField(null=True)
    membership = models.CharField(
        max_length=1, choices=MEMEBERSHIP_CHOICES, default=MEMEBERSHIP_BRONZE)
