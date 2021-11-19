from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Pokemon

# Create your views here.

class SelectView(generic.DetailView):
    model = Pokemon
    template_name = 'pokemon_letter/select.html'
