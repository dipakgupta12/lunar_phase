from rest_framework import response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication

from rest_framework import views
from rest_framework.response import Response
from .serializers import LunarPhaseSerializer
import requests
import datetime

class LunarPhaseAPI(views.APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication]
    serializer_class = LunarPhaseSerializer

    def get(self, request):
        client_id = "l7pvr11WSU0FpD62gkVNM"
        client_secret = "o1XrQWGQdCshIYfqthufvrOKhprFOked7r8mQEyk"
        moon_api = f"https://api.aerisapi.com/sunmoon/moonphases/?client_id={client_id}&client_secret={client_secret}"

        response = requests.get(moon_api)
        data = response_data = response.json()
        if data['success']:
            code = data['response'][0]['code']
            timestamp = data['response'][0]['timestamp']
            name = data['response'][0]['name']

            lunar_datetime = datetime.datetime.fromtimestamp(timestamp)
            now = datetime.datetime.now()

            timedelta = lunar_datetime - now

            if timedelta.days:
                if code == 0:
                    code = 0.5
                    name = "waning crescent"
                elif code == 1:
                    code = 1.5
                    name = "waxing crescent"
                elif code == 2:
                    code = 2.5
                    name = "waxing gibbous"
                elif code == 3:
                    code = 3.5
                    name = "waning gibbous"
                
            response_data = {
                "status": data["success"],
                "error": None,
                'response': {
                    'code': code,
                    'name': name
                }
            }

        return Response(response_data)
