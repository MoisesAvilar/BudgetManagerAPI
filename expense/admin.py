from django.contrib import admin
from expense.models import Expense


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "description",
        "value",
        "amount",
        "created_at",
        "updated_at",
        "total",
    )
