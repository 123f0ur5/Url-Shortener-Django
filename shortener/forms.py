from django import forms
from .models import Url

class UrlForm(forms.Form):
	model = Url
	original_link	= forms.CharField(label='Your Link', widget=forms.TextInput(attrs={"placeholder" : "Your Link"}))