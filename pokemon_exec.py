import os 	#장고 모듈/패키지 사용을 위한 세팅
os.environ.setdefault('DJANGO_SETTINGS_MODULE','programming.settings')
import django
django.setup()
from pokemon.models import Pokemon, Human, Catch

hum = Human.objects.get_or_create(name="Jiwoo")
ind = Human.objects.filter().count()
print('현재 등록된 포켓몬 트레이너는 다음과 같습니다.')
print(list(Human.objects.filter().values()[i]['name'] for i in range(0,ind)))
ans = input('추가하시겠습니까?(y/n) :')

while True:
	if ans == 'y':
		iname = input('트레이너 이름 : ')
		hum=Human.objects.get_or_create(name=iname)
		ind = Human.objects.filter().count()
		print('현재 등록된 포켓몬 트레이너는 다음과 같습니다.')
		print(list(Human.objects.filter().values()[i]['name'] for i in range(0,ind)))
		ans = input('계속 추가하시겠습니까?(y/n)')
	elif ans =='n':
		break
	else:
		break

while 1:
	print('누가 어떤 포켓몬을 잡았는지 적어주세요.')
	who = input('트레이너 : ')
	wha = input('포켓몬 : ')
	pos = input('위치 : ')

	chum = Human.objects.get(name=who)
	cmon = Pokemon.objects.get(name=wha)
	cat = Catch.objects.get_or_create(human=chum,monster=cmon,position=pos)
	chum.monster.add(cmon)
	print(chum.monster.values())
	if input('추가로 이벤트를 입력하시겠습니까?(y/n)') != 'y':
		break
