from django.contrib import admin
from django.urls import path
from django.contrib.admin import site
from django.urls.conf import include
from hero.views_hero import SignUpView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', SignUpView.as_view(), name='signup'),

    path('', include('hero.urls')),
    
    path('', include('article.urls')),
]
