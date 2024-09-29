from django.db import models
from django.core.exceptions import ValidationError
from planner.models import Planner


class Item(models.Model):
    planner = models.ForeignKey(Planner, related_name='items', on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    amount = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=2)

    def clean(self):
        if self.value < 0:
            raise ValidationError("The value cannot be negative.")

    def __str__(self):
        return self.description

    @property
    def total(self):
        return self.amount * self.value
