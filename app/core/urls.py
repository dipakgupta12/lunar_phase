from django.urls import path
from .views import LunarPhaseView
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('', login_required(LunarPhaseView.as_view()), name="lunar_phase"),
]