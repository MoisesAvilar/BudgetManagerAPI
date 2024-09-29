from django.urls import path
from item.views import ItemCreateListView, ItemRetrieveUpdateDestroyView


urlpatterns = [
    path("list/<int:planner_id>/item/", ItemCreateListView.as_view(), name="item-create-list-view"),
    path(
        "list/<int:planner_id>/item/<int:pk>/",
        ItemRetrieveUpdateDestroyView.as_view(),
        name="item-detail-view",
    ),
]
