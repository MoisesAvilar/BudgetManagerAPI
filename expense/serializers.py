from expense.models import Expense
from rest_framework import serializers


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Expense
