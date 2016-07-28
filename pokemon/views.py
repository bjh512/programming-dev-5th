from django.shortcuts import render
from pokemon.models import Pokemon

def pokemon_list(request):
	qs = Pokemon.objects.all()
	return render(request, 'pokemon/pokemon_list.html',{'pokemon_list':qs,})