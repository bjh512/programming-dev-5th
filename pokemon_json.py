import os 	#장고 모듈/패키지 사용을 위한 세팅
os.environ.setdefault('DJANGO_SETTINGS_MODULE','programming.settings')
import django,json
django.setup()
from pokemon.models import Pokemon

with open ('pokemon/pokemon.json') as p:
	jdata = json.loads(p.read())
mon = [Pokemon.objects.get_or_create(name=jdata[i]["name"],typ=jdata[i]["type"],num=i)
 for i in jdata]