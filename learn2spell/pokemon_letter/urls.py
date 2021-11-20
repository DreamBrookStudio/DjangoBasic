from django.urls import path

from . import views

app_name = 'pokemon_letter'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pokemon_id>/', views.select, name='select'),
    path('random_pokemon/', views.random_pokemon, name='random_pokemon'),
    path('next_pokemon/<int:pokemon_id>/', views.next_pokemon, name='next_pokemon'),

]