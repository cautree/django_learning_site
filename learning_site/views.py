from django.shortcuts import render


#from .forms import SuggestionForm
from . import forms


def hello_world(request):
	return render(request, 'home.html')


def suggestion_view(request):
	form = forms.SuggestionForm()
	return render(request, 'suggestion_form.html', {'form':form})
