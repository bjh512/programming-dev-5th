import re
from django.db import models
from django.forms import ValidationError

def position_validator(value):
	if not re.match(r'^(\d*),(\d*)$',value):
		raise ValidationError('Invalid Position Type')

class Pokemon(models.Model):
	name = models.CharField(max_length=50)
	typ = models.CharField(max_length=20)
	num = models.IntegerField()
	def __str__(self):
		return self.name	

class Human(models.Model):
	name = models.CharField(max_length=50)
	cnt = models.IntegerField(default = 0)
	monster = models.ManyToManyField(Pokemon,related_name='monster')
	def __str__(self):
		return self.name	

class Catch(models.Model):
	human = models.ForeignKey(Human)
	monster = models.ForeignKey(Pokemon)
	position = models.CharField(max_length=30,validators=[position_validator],
		help_text='x,y 포맷으로 입력')
