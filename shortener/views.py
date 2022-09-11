from django.shortcuts import render, redirect
from .models import Url
from .forms import UrlForm
import string, random

# Create your views here.
def home_view(request, *args, **kwargs):
	my_url = UrlForm(request.POST or None)
	if my_url.is_valid():
		link = request.POST.get('original_link')
		link = fix_link(link)
		identify = generate_identifier()
		Url.objects.create(original_link=link, identifier=identify)
		return redirect('shorten/'+identify, identify)
		my_url = UrlForm()
	context = {
		'my_url' : my_url,
	}
	return render(request, "home.html", context)

def dynamic_lookup_view(request, identify):
	url = Url.objects.get(identifier=identify)
	context = {
		"my_url" : url
	}
	return render(request, "shorten_view.html", context)

def shorten_link(request, identify):
	context = {
		'my_identifier' : identify
	}
	return render(request, "shorten_url.html", context)

def generate_identifier(size = 5, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
	identify = ''.join(random.choice(chars) for _ in range(size))
	while Url.objects.filter(identifier=identify).exists():
		identify = ''.join(random.choice(chars) for _ in range(size))

	return identify

def fix_link(link):
	if 'www' not in link:
		link = 'www.' + link
	if 'http://' not in link:
		link = 'http://' + link

	return link