from django.views.generic import TemplateView


class LunarPhase(TemplateView):
    template_name = 'core/lunar_phase.html'
