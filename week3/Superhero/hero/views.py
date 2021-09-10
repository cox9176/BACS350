from django.views.generic import TemplateView

class SupermanView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'hero': 'superman', 
        }

class BatmanView(TemplateView):
    template_name = "hero.html"

    def get_context_data(self, **kwargs):
        return {
            'hero': 'batman', 
        }

class WonderWomanView(TemplateView):
    template_name = "hero.html"

    def get_context_data(self, **kwargs):
        return {
            'hero': 'wonder_woman', 
        }

class HomeView(TemplateView):
    template_name = "profile.html"
