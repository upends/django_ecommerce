from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, blank=True)
    contact_no = models.CharField(max_length=13,blank=True)
    address_line = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    zip_code = models.CharField(max_length=10, blank=True)
    country = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return f"{self.address_line}, {self.city}, {self.state} {self.zip_code}, {self.country}"
    
    def getAddress(self):
        return f"{self.address_line}, {self.city}, {self.state} {self.zip_code}, {self.country}"