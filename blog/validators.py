import re
from django.forms import ValidationError

class MinLengthValidator(object):
	def __init__(self,min_length):
		self.min_length = min_length

	def __call__(self,value):
		if len(value) < self.min_length:
			raise ValidationError('{}글자 이상 입력해주세요.'.format(self.min_length))

def phone_number_validator(self, value):
	if not re.match(r'^01[016789][1-9]\d{6,7}$', value):
		raise ValidationError('휴대폰 번호를 입력해주세요.')
