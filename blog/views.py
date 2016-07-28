from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post
from pokemon.models import Pokemon

def post_list(request):
	return render(request, 'blog/post_list.html',{'post_list':Post.objects.all()})

def poke_list(request):
	return render(request, 'blog/post_list.html',{'poke_list':Pokemon.objects.all()})

def mysum(request,x,y=0,z=0):
	return HttpResponse(int(x) + int(y)+ int(z))

def mysum2(request,x):
	result = sum(int(i) for i in x.split('/'))
	return HttpResponse(result)