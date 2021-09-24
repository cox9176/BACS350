from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Superhero

class HeroListView(ListView):
    model = Superhero
    template_name = 'hero_list.html'

class HeroDetailView(DetailView):
    model = Superhero
    template_name = 'hero_detail.html'
