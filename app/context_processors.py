from random import choice
from django.core.urlresolvers import reverse

frases=['esta es una frase al azar','tengo hambre', 'me gusta ale','enserio ale?']

def ejemplo(request):
	return {'frase': choice(frases)}

def menu(request):
	menu = {'menu': [
		{'name':'Home','url':reverse('index')},
		{'name': 'Add','url':reverse('add')},
		{'name': 'Acerca de','url':reverse('about')},
		{'name': 'Enlaces','url':reverse('enlaces')},
	]}
	for item in menu['menu']:
		if request.path == item['url']:
			item['active'] = True
	return menu