from rest_framework import response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from rest_framework import views
from rest_framework.response import Response

from django.conf import settings
from core.lunar_phases import LunarPhase

class LunarPhaseAPI(views.APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication]

    def get(self, request):
        lunar_phase = LunarPhase()
        data = lunar_phase.get_optimized_data()
        return Response(data)

