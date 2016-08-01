from django.shortcuts import render
from pokemon.models import Pokemon
from pokemon.models import Human, Catch

def pokemon_list(request):
	qs = Pokemon.objects.all()
	return render(request, 'pokemon/pokemon_list.html',{'pokemon_list':qs,})

def human_list(request):
	qs = Human.objects.all()
	return render(request,'pokemon/human_list.html',{'human_list':qs,})

def catch_list(request):
	qs = Catch.objects.all()
	return render(request,'pokemon/catch_list.html',{'catch_list':qs,})