from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, RedirectView, CreateView, UpdateView, DeleteView
from .models import Profile

class ProfileCreateView(LoginRequiredMixin, CreateView):
    model = Profile
    template_name = 'profile_add.html'
    fields = ['superhero', 'identity', 'image', 'description', 'strength', 'weakness']

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    template_name = 'profile_edit.html'
    fields = ['superhero', 'identity', 'image', 'description', 'strength', 'weakness']
