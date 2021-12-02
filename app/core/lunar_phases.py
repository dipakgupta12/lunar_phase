
from django.conf import settings
import requests
from requests.models import Response

import datetime

class LunarPhase:

    def __init__(self):
        client_id = settings.ARIS_CLIENT_ID
        client_secret = settings.ARIS_CLIENT_SECRET
        self.moon_api = f"https://api.aerisapi.com/sunmoon/moonphases/?client_id={client_id}&client_secret={client_secret}"

    def get_current_phase_response(self):
        response = requests.get(self.moon_api)
        res_data = response.json()
        return res_data

    def get_optimized_data(self):
        data = self.get_current_phase_response()
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
                    'id': name.replace(' ', '_'),
                    'code': code,
                    'name': name
                }
            }
        else:
            response_data = {
                "status": data["success"],
                "error": data["error"],
                'response': None
            }
        return response_data
