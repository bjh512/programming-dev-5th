#Post에 저장되어있는 데이터들 중 title이 가장 긴 것 혹은 짧은 것, 또는 test_field의 값이 가장 큰 것과 작은 것을 출력하는 코드입니다.
import os 	#장고 모듈/패키지 사용을 위한 세팅 시작
os.environ.setdefault('DJANGO_SETTINGS_MODULE','programming.settings')
import django
django.setup()	#세팅 끝
from blog.models import Post	#blog.models라는 파일을 통해 원하는 DB import

lazy = Post.objects.filter()	#DB로부터 모든 instance를 불러 오게 하고 그것을 lazy로 선언
								#하지만 컴퓨터는 실제로 이 단계에서 query를 쏘아 DB에 접근하지는 않는다. lazy하게 작동하는 것이 보다 효율적이기 때문.
li=[]	# 각 instance의 타이틀의 길이 혹은 test_field의 값이 저장될 리스트 선언
inp=input('Enter a category (title/test_field) :')	#입력
if(inp=='title'):	#title이 가장 긴 것, 짧은 것을 출력하고자 하는 경우
	for instance in lazy.values():	#lazy.values는 모든 instance들을 다 불러오기 때문에 그 중 하나씩 보기 위해 첫번째 for문 사용.
									#실제로 query를 쏘아 접근을 시작하는 단계
		for field in instance:	#instance들의 전체 field들이 불러 와 있는 상태에서 하나의 for문을 고르기 위한 두번째 for문.
			if field=='title':	#field명들을 보다가 title이라는게 걸렸을 때 
				li.append(len(instance[field]))	#그 title의 길이들을 하나씩 리스트에 추가한다.
	print('\n<The Longest Title Post>')	
	for i,j in Post.objects.filter(id=li.index(max(li))+1).values()[0].items():	#그 리스트 중 최댓값의 인덱스를 반환하여 그 것을 id로 하는 instance의 전체 값들을 i,j에 하나씩 받아 출력
																				#+1을 하는 이유는 id는 1부터 시작하므로. [0]을 하는 이유는 그냥 values는 list 안에 dictionary가 있는 형태로 값을 return시키므로.																			
		print(i,'=',j)
	print('\n<The Shortest Title Post>')
	for i,j in Post.objects.filter(id=li.index(min(li))+1).values()[0].items():	#상기 동일한 작업으로 최솟값 출력
			print(i,'=',j)
elif(inp=='test_field'):	#test_field 값이 가장 큰 것과 작은 것을 출력하고자 하는 경우
	for instance in lazy.values():	#상기한 작업과 동일. 만약 user가 test_field라고 입력을 했다면 여기가 실제 query를 함으로써 DB에 접근하는 첫 단계
		for field in instance:
			if field=='test_field':
				li.append(instance[field])
	print('\n<The Largest test_field Post>')
	for i,j in Post.objects.filter(id=li.index(max(li))+1).values()[0].items():
		print(i,'=',j)
	print('\n<The Smallest test_field Post>')
	for i,j in Post.objects.filter(id=li.index(min(li))+1).values()[0].items():
		print(i,'=',j)
else:	#일종의 예외처리
	print('Please enter title or test_field!')