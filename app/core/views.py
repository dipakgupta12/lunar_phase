from django.views.generic import TemplateView


class LunarPhaseView(TemplateView):
    template_name = 'core/lunar_phase.html'
