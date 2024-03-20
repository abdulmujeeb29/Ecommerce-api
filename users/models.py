from django.db import models
from django.contrib.auth.models import User 
from django.contrib.auth import get_user_model
User=get_user_model()

# Create your models here.





class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=20)

    def __str__(self):
        return f"Address for {self.user.username}"