from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from earning.category import CATEGORY


class Earning(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_earning", default=1
    )
    description = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices=CATEGORY)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        if self.value < 0:
            raise ValidationError("The value cannot be negative.")

    def __str__(self):
        return self.description.title()

    @property
    def total(self):
        return self.value * self.amount
