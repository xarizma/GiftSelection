from django import forms
from .models import *
class TagForm(forms.ModelForm):

	class Meta:
		model = Tags
		exclude = [""]