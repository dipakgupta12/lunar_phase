from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication

from rest_framework import generics
from .serializers import LunarPhaseSerializer
from core.models import LunarPhase


class LunarPhaseAPI(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication]
    serializer_class = LunarPhaseSerializer
    queryset = LunarPhase.objects.all()
