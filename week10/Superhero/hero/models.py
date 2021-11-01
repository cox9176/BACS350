from django.db import models
from django.urls.base import reverse_lazy
from django.contrib.auth.models import User

class Superhero(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

class Profile(models.Model):
    superhero = models.ForeignKey(Superhero, on_delete=models.CASCADE)
    identity = models.CharField(max_length=100)
    image = models.CharField(max_length=100, default='None')
    description = models.TextField(default='None')
    strength = models.CharField(max_length=100, default='None')
    weakness = models.CharField(max_length=100, default='None')

    def __str__(self):
        return f'{self.identity}'

    def get_absolute_url(self):
        return reverse_lazy('hero_detail', args=[str(self.id)])
