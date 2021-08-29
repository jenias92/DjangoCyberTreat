from django.db import models
from django.urls import reverse


class Customer(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    birthday = models.DateField()
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.last_name

    def get_absolute_url(self):
        return reverse('customer-detail', kwargs={'pk': self.pk})
