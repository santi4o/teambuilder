from django.shortcuts import redirect, render
from users.models import Task
from .forms import PersonalityTestForm
from json import loads
from urllib import request

data = None
with request.urlopen("https://jdavidpm.github.io/my-static-files/teamBuilder/json/hexaco_items.json") as url:
	data = loads(url.read().decode(encoding='utf-8'))

def index(request):
	tasks_list = Task.objects.all()
	context = {
		'tasks': tasks_list
	}
	return render(request, 'layout/index.html', context)

def faq(request):
	return render(request, 'layout/faq.html', {'title': 'Preguntas Frecuentes'})

def about(request):
	return render(request, 'layout/about.html', {'title': 'Acerca de'})

def tools(request):
	return render(request, 'layout/tools.html', {'title': 'Herramientas'})

def hexaco_test(request):
	dict_facets = {'H':0, 'E':0, 'X':0, 'A':0, 'C':0, 'O':0}
	if request.method == 'POST':
		form = PersonalityTestForm(request.POST)
		if form.is_valid():
			for i in range(1, 61):
				facet, sub_facet, is_reversed = data[i - 1]['statement_facet'].split(', ')
				dict_facets[facet] += int(form.cleaned_data['statement_' + str(i)])
			dict_facets = {f: dict_facets[f] / 10 for f in dict_facets}
			current_user = request.user
			for f in dict_facets:
				setattr(current_user.profile, 'personality_' + f.lower(), dict_facets[f])
			current_user.save()
			return redirect('layout-index')

	# if a GET (or any other method) we'll create a blank form
	else:
		form = PersonalityTestForm()
	return render(request, 'layout/hexaco_test.html', {'title': 'Test de Personalidad', 'form': form})