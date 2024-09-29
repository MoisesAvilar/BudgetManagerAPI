from django.urls import path
from earning.views import EarningCreateListView, EarningRetrieveUpdateDestroyView


urlpatterns = [
    path("earnings/", EarningCreateListView.as_view(), name="earning-create-list-view"),
    path(
        "earnings/<int:pk>/",
        EarningRetrieveUpdateDestroyView.as_view(),
        name="earning-detail-view",
    ),
]
