from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, RedirectView, CreateView, UpdateView, DeleteView
from .models import Superhero, Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'registration/signup.html'

class HeroRedirectView(RedirectView):
    url = '/hero/'

class HeroListView(ListView):
    model = Superhero
    template_name = 'hero_list.html'

class HeroDetailView(DetailView):
    model = Superhero
    template_name = 'hero_detail.html'

    def get_context_data(self, **kwargs):
        superhero = Superhero.objects.get(pk=self.kwargs['pk'])
        return dict(object=superhero, profiles=Profile.objects.filter(superhero=superhero.id))

class HeroCreateView(LoginRequiredMixin, CreateView):
    model = Superhero
    template_name = 'hero_add.html'
    fields = ['name']
    success_url = reverse_lazy('hero_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class HeroUpdateView(LoginRequiredMixin, UpdateView):
    model = Superhero
    template_name = 'hero_edit.html'
    fields = ['name']
    success_url = reverse_lazy('hero_list')

class HeroDeleteView(LoginRequiredMixin, DeleteView):
    model = Superhero
    template_name = 'hero_delete.html'
    success_url = reverse_lazy('hero_list')
