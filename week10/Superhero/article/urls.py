from django.views.generic import RedirectView
from django.urls.conf import include
from django.contrib import admin
from django.urls import path
from .views import DocumentView

urlpatterns = [
    path('article/', DocumentView.as_view(), name='document'),
    path('article/<str:article>', DocumentView.as_view())
]
