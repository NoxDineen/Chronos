from django import forms
from timekeeper.chronos.models import Assignment, Person

class AssignmentForm(forms.ModelForm):
	class Meta:
		model = Assignment

class PersonForm(forms.ModelForm):
	class Meta:
		model = Person