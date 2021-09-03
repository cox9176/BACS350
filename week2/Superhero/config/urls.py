from django.urls import path
from hero.views import SupermanView, BatmanView, WonderWomanView

urlpatterns = [
    path('superman', SupermanView.as_view()),
    path('batman', BatmanView.as_view()),
    path('wonderwoman', WonderWomanView.as_view()),
]
