from django.shortcuts import render
from post.models import Address
from post.postcode import search_zipcode

def post_list(request):
	li=[]
	for i in Address.objects.all():
		li.append(search_zipcode(i))

	return render(request,'post/post_list.html',{'post_list':Address.objects.all(),'addr_list':li})