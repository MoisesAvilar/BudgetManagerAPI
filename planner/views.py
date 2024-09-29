from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from planner.models import Planner
from planner.serializers import PlannerSerializer


class PlannerCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PlannerSerializer

    def get_queryset(self):
        return Planner.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PlannerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PlannerSerializer

    def get_queryset(self):
        return Planner.objects.filter(user=self.request.user)
