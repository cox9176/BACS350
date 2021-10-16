from django.db import models
from django.urls.base import reverse_lazy

class Superhero(models.Model):
    name = models.CharField(max_length=100)
    identity = models.CharField(max_length=100)
    image = models.CharField(max_length=100, default='None')
    description = models.TextField(default='None')
    strength = models.CharField(max_length=100, default='None')
    weakness = models.CharField(max_length=100, default='None')

    def __str__(self):
        return f'{self.pk} - {self.name}'

    def get_absolute_url(self):
        return reverse_lazy('hero_detail', args=[str(self.id)])
