from django.db import models

class Person(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.EmailField(max_length=255)
	is_support = models.BooleanField(default=False)

	class Meta:
		verbose_name_plural = 'people'

	def __unicode__(self):
		return u'%s %s' % (self.first_name, self.last_name)

class Assignment(models.Model):
	date = models.DateField(auto_now=False)
	person = models.ForeignKey('chronos.Person')
	role = models.ForeignKey('chronos.Role', default='Support')	

	class Meta:
		unique_together = ('date', 'person')

	def __unicode__(self):
		return u'%s %s on %s (%s)' % (self.person.first_name, self.person.last_name, self.date, self.role)

class Role(models.Model):
	name = models.CharField(max_length=255)
	icon = models.FileField(upload_to='chronos', blank=True)

	def __unicode__(self):
		return self.name