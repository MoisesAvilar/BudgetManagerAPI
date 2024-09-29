from planner.models import Planner
from rest_framework import serializers


class PlannerSerializer(serializers.ModelSerializer):
    total_items = serializers.SerializerMethodField()

    class Meta:
        fields = '__all__'
        model = Planner

    def get_total_items(self, obj):
        return obj.items.count()
