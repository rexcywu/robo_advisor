from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Stocks(models.Model):
    symbol = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    buying_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    coin = models.BooleanField(default=False)

    def __str__(self):
        return self.symbol

    def get_absolute_url(self):
        return reverse('portfolio-home')

    def save(self, *args, **kwargs):
        # convert all symbol to uppercase
        self.symbol = self.symbol.upper()
        return super().save(*args, **kwargs)