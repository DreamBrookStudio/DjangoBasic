from django.db import models
from random import sample, shuffle
# Create your models here.

class Pokemon(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    image = models.ImageField()

    def get_letters(self, N, i):
        first = self.name[0]
        alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        alphabet.remove(first)
        letters = sample(alphabet,3) + [first]
        shuffle(letters)
        return letters

    def __str__(self):
        return self.name
