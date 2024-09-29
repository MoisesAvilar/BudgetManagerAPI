from django.db import models
from django.contrib.auth.models import User
from planner.category import CATEGORY


class Planner(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY)
    spending_target = models.DecimalField(decimal_places=2, max_digits=10, default=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description

    @property
    def total_items(self):
        return self.items.count()
