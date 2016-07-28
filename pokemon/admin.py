from django.contrib import admin
from pokemon.models import Pokemon,Human,Catch

class CatchAdmin(admin.ModelAdmin):
	list_display = ['get_hname','get_mname','position']
	def get_mname(self,obj):
		return obj.monster.name
	def get_hname(self,obj):
		return obj.human.name
	get_hname.short_description = 'Human Name'
	get_mname.short_description = 'Monster Name'	

class PokeAdmin(admin.ModelAdmin):
	list_display= ['num','name','typ']
	
class HumAdmin(admin.ModelAdmin):
	list_display= ['pk','name','get_mon']
	def get_mon(self,obj):
		return obj.monster.get().name
		
admin.site.register(Catch,CatchAdmin)
admin.site.register(Pokemon,PokeAdmin)
admin.site.register(Human,HumAdmin)