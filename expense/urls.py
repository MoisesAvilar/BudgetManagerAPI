from django.urls import path
from expense.views import ExpenseCreateListView, ExpenseRetrieveUpdateDestroyView


urlpatterns = [
    path("expense/", ExpenseCreateListView.as_view(), name="expense-create-list-view"),
    path(
        "expense/<int:pk>/",
        ExpenseRetrieveUpdateDestroyView.as_view(),
        name="expense-detail-view",
    ),
]
