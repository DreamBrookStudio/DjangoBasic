from django.urls import path

from . import views

app_name = 'pokemon_letter'
urlpatterns = [
    path('<int:pk>/', views.SelectView.as_view(), name='select')
]