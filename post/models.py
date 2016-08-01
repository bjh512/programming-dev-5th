from django.db import models
import re
from django.forms import ValidationError

def postal_code_validator(value):
		if not re.match(r'^[0-6]\d{4}$', value):
			raise ValidationError('올바른 우편번호가 아닙니다.')
	
class Address(models.Model):
	addr = models.CharField(max_length=200, validators=[postal_code_validator],help_text='우편번호 5자리')
	def __str__(self):
		return self.addr