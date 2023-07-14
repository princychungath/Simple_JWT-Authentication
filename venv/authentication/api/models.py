from django.db import models
from django.contrib.auth.models import AbstractUser


class Customer(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']


class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(Customer, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
