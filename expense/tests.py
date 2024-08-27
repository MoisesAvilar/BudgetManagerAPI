from django.test import TestCase
from .models import Expense
from django.utils import timezone
from django.core.exceptions import ValidationError


class ExpenseModelTest(TestCase):

    def setUp(self):
        # Create an instance
        self.expense = Expense.objects.create(
            description="Compra de Equipamento",
            value=100.00,
            amount=2,
            date=timezone.now()
        )

    def test_expense_creation(self):
        # Verify if expense was created
        self.assertIsInstance(self.expense, Expense)
        self.assertEqual(self.expense.description, "Compra de Equipamento")
        self.assertEqual(self.expense.value, 100.00)
        self.assertEqual(self.expense.amount, 2)

    def test_expense_total(self):
        # Verify if property total is working normally
        self.assertEqual(self.expense.total, 200.00)

    def test_expense_negative_value(self):
        # Verify if value is negative
        expense = Expense(
            description="Compra de Equipamento",
            value=-100.00,
            amount=1,
            date=timezone.now()
        )
        with self.assertRaises(ValidationError):
            expense.full_clean()
            expense.save()
