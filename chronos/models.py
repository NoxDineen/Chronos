from django.db import models
from django.contrib.auth.models import User

class Person(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.EmailField(max_length=255)
	is_support = models.BooleanField(default=False)
	user = models.ForeignKey(User, unique=True)

	class Meta:
		verbose_name_plural = 'people'

	def __unicode__(self):
		return self.email

class Assignment(models.Model):
	date = models.DateField
	person = models.ForeignKey('chronos.Person')	

	class Meta:
		unique_together = ('date', 'person')

	def __unicode__(self):
		return self.date

class Role(models.Model):
	name = models.CharField(max_length=255)
	assignment = models.ManyToManyField('chronos.Assignment')
	icon = models.ImageField(upload_to='chronos')

	def __unicode__(self):
		return self.name