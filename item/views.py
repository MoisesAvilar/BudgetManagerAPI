from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from item.models import Item
from item.serializers import ItemSerializer
from planner.models import Planner


class ItemCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ItemSerializer

    def get_queryset(self):
        planner_id = self.kwargs['planner_id']
        return Item.objects.filter(planner_id=planner_id)

    def perform_create(self, serializer):
        planner = get_object_or_404(Planner, id=self.kwargs['planner_id'])
        serializer.save(user=self.request.user, planner=planner)


class ItemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ItemSerializer

    def get_queryset(self):
        planner_id = self.kwargs['planner_id']
        return Item.objects.filter(planner_id=planner_id)
