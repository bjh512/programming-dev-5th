import re
from django.db import models
from django.forms import ValidationError
from django.utils import timezone
from .validators import MinLengthValidator
from .fields import PhoneNumberField

def lnglat_validator(value):
	if not re.match(r'^(\d+\.?\d*),(\d+\.?\d*)$',value):
		raise ValidationError('Invalid LngLat Type')
'''
def min_len_validator(mlen):
	def wrap(value):
		if len(value) < mlen :
			raise ValidationError('{}글자 이상 입력하시오'.format(mlen))
	return wrap
'''
min_len_4_validator = MinLengthValidator(4)

class Post(models.Model):
	title = models.CharField(max_length=100, verbose_name='제목',validators=[min_len_4_validator])
	content = models.TextField(help_text='Markdown 문법을 써주세요.')
	#tags = models.CharField(max_length=100, blank=True)
	tag_set = models.ManyToManyField('Tag',blank=True)
	lnglat = models.CharField(max_length=50, 
		validators=[lnglat_validator],
		help_text='경도,위도 포맷으로 입력')
	created_at = models.DateTimeField(default=timezone.now)
	test_field = models.IntegerField(default=10)

class Tag(models.Model):
	name = models.CharField(max_length=20)

	def __str__(self):
		return self.name

class Contact(models.Model):
	name=models.CharField(max_length=20)
	phone = PhoneNumberField()