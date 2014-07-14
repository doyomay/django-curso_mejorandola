from django.shortcuts import redirect
from random import choice

paises  = ['col','mx','eu','uk']
def de_donde_vengo(request):
	return choice(paises)

class PaisMiddleware():
	def process_request(self, request):
		pais = de_donde_vengo(request)
		#print pais
		if pais == 'ms': ## 'mx'
			return redirect('http://mejorando.la')