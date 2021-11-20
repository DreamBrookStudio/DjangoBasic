from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Pokemon

# Create your views here.

from random import choice

def random_pokemon(request):
    pks = Pokemon.objects.values_list('pk', flat=True)
    pokemon = Pokemon.objects.get(pk=choice(pks))
    return HttpResponseRedirect(reverse('pokemon_letter:select', args=(pokemon.id,)))

def next_pokemon(request, pokemon_id):
    next_id = pokemon_id + 1
    if next_id > len(Pokemon.objects.values_list('pk', flat=True)):
        next_id = 1
    return HttpResponseRedirect(reverse('pokemon_letter:select', args=(next_id,)))

def index(request):
    return render(request, 'pokemon_letter/index.html')

def select(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, pk=pokemon_id)
    context = {'pokemon': pokemon,
               'letters': pokemon.get_letters(0,0)}
    return render(request, 'pokemon_letter/select.html', context)

class SelectView(generic.DetailView):
    model = Pokemon
    template_name = 'pokemon_letter/select.html'
    extra_context = {'letters': ["1","a","c"]}