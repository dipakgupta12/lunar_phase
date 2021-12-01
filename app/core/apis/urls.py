from django.urls import path
from .views import LunarPhaseAPI
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('lunar_phase', LunarPhaseAPI.as_view(), name="lunar_phase_api"),
]