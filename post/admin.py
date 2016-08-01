from django.contrib import admin
from post.models import Address
'''
class AddressAdmin(admin.ModelAdmin):
	list_display=['pk']
'''
admin.site.register(Address)