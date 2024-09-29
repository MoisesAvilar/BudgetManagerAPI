from django.contrib import admin
from earning.models import Earning


@admin.register(Earning)
class EarningAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "description",
        "category",
        "value",
        "amount",
        "created_at",
        "updated_at",
        "total",
    )
