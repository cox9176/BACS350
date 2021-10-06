from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, RedirectView, CreateView, UpdateView, DeleteView
from .models import Superhero

class HeroRedirectView(RedirectView):
    url = '/hero/'

class HeroListView(ListView):
    model = Superhero
    template_name = 'hero_list.html'

class HeroDetailView(DetailView):
    model = Superhero
    template_name = 'hero_detail.html'

class HeroCreateView(LoginRequiredMixin, CreateView):
    model = Superhero
    template_name = 'hero_add.html'
    fields = ['name', 'identity', 'image', 'description', 'strength', 'weakness']

class HeroUpdateView(LoginRequiredMixin, UpdateView):
    model = Superhero
    template_name = 'hero_edit.html'
    fields = ['name', 'identity', 'image', 'description', 'strength', 'weakness']

class HeroDeleteView(LoginRequiredMixin, DeleteView):
    model = Superhero
    template_name = 'hero_delete.html'
    success_url = reverse_lazy('hero_list')
