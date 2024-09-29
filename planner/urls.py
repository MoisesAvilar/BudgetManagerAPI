from django.urls import path
from planner.views import PlannerCreateListView, PlannerRetrieveUpdateDestroyView


urlpatterns = [
    path("list/", PlannerCreateListView.as_view(), name="planner-create-list-view"),
    path(
        "list/<int:pk>/",
        PlannerRetrieveUpdateDestroyView.as_view(),
        name="planner-detail-view",
    ),
]
