from django.urls import path
from earning.views import EarningCreateListView, EarningRetrieveUpdateDestroyView


urlpatterns = [
    path("earning/", EarningCreateListView.as_view(), name="earning-create-list-view"),
    path(
        "earning/<int:pk>/",
        EarningRetrieveUpdateDestroyView.as_view(),
        name="earning-detail-view",
    ),
]
