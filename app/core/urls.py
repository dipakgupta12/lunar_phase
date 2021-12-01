from django.urls import path
from .views import LunarPhase
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('', login_required(LunarPhase.as_view()), name="lunar_phase"),
]