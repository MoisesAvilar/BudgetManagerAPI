from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from earning.models import Earning
from earning.serializers import EarningSerializer


class EarningCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = EarningSerializer

    def get_queryset(self):
        return Earning.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class EarningRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = EarningSerializer

    def get_queryset(self):
        return Earning.objects.filter(user=self.request.user)
