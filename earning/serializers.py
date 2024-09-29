from earning.models import Earning
from rest_framework import serializers


class EarningSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Earning
