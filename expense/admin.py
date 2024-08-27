from django.contrib import admin
from expense.models import Expense


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('description', 'value', 'amount', 'date', 'total')
