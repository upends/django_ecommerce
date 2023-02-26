from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal
# Create your models here.

class Product(models.Model):
    sku = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    short_description = models.TextField()
    long_description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)

    def __str__(self):
        return self.name
    

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Product)
    subtotal = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)

    def __str__(self):
        return f"{self.user.username}'s Cart"

