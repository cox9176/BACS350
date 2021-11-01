from .views_hero import HeroListView, HeroDetailView, HeroRedirectView, HeroCreateView, HeroUpdateView, HeroDeleteView
from .views_profile import ProfileCreateView, ProfileUpdateView
from django.urls.conf import include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', HeroRedirectView.as_view(), name='home'),
    path('hero/', HeroListView.as_view(), name='hero_list'),
    
    path('hero/<int:pk>', HeroDetailView.as_view(), name='hero_detail'),
    path('hero/add', HeroCreateView.as_view(), name='hero_add'),
    path('hero/<int:pk>/', HeroUpdateView.as_view(), name='hero_edit'),
    path('hero/<int:pk>/delete', HeroDeleteView.as_view(), name='hero_delete'),

    path('profile/add', ProfileCreateView.as_view(), name='profile_add'),
    path('profile/<int:pk>', ProfileUpdateView.as_view(), name='profile_edit'),
]
