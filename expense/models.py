from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


class Expense(models.Model):
    description = models.CharField(max_length=50)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.IntegerField(default=1)
    date = models.DateTimeField(default=timezone.now)

    def clean(self):
        if self.value < 0:
            raise ValidationError('The value cannot be negative.')

    def __str__(self):
        return self.description.title()

    @property
    def total(self):
        return self.value * self.amount
