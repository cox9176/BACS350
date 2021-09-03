from django.views.generic import TemplateView

class SupermanView(TemplateView):
    template_name = 'superman.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'About this Class', 
            'body': 'Once upon a time ...',
        }

class BatmanView(TemplateView):
    template_name = "batman.html"

class WonderWomanView(TemplateView):
    template_name = "wonder_woman.html"
