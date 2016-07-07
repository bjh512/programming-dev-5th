import re
a=input('')
if re.match(r'^01[016789][1-9]\d{6,7}$',a):
	print('전화번호가 맞습니다.')
else:
	print('전화번호가 아닙니다.')