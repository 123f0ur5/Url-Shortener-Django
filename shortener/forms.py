from django import forms
from .models import Url

class UrlForm(forms.ModelForm):
	original_link	= forms.CharField(label='Your Link', widget=forms.TextInput(attrs={"placeholder" : "Your Link"}))
	
	class Meta:
		model = Url
		fields = [
			'original_link',
		]

	def clean_original_link(self):
		original_link = self.cleaned_data.get("original_link")
		if '.' not in original_link:
			raise forms.ValidationError("Insert a valid Link")
		else:
			return original_link