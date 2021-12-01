from rest_framework import serializers
from core.models import LunarPhase


class LunarPhaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = LunarPhase
        fields = "__all__"
