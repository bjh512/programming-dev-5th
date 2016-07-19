from django.contrib import admin
from pokemon.models import Pokemon,Human,Catch

class PokeAdmin(admin.ModelAdmin):

	list_display = ['get_hname','get_mname','position']

	def get_mname(self,obj):
		return obj.monster.name
	def get_hname(self,obj):
		return obj.human.name

	get_hname.short_description = 'Human Name'
	get_mname.short_description = 'Monster Name'	
	
admin.site.register(Catch,PokeAdmin)
