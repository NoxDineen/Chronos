from django import forms
from chronos.models import Assignment

class AssignmentForm(forms.ModelForm):
	class Meta:
		model = Assignment