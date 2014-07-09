
from django.shortcuts import render_to_response, get_object_or_404

from django.template.context import RequestContext
from django.http import HttpResponseRedirect

from datetime import datetime

from models import *
from forms import *

from django.contrib.auth.decorators import login_required
# Create your views here.
"""
-- Manera Larga

from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from datetime import datetime

def hora_actual(request):
	ahora = datetime.now() 			### Con ayuda de la libreria obtenemos la fecha
	t = get_template('hora.html')	### Obtenemos el tempalte
	c = Context({"hora":ahora,"usuario":"gerardo"}) ### dentro del contenido, pasamos las variables a usar en dict
	html = t.render(c) ### renderizamos el template anterior
	return HttpResponse(html) ###regresamos por el response el html
"""
def hora_actual(request):
	now = datetime.now()
	return render_to_response('hora.html',{'hora':now,'usuario':'Gerardo'})

def index(request):
	categorias = Categoria.objects.all()
	enlaces	= Enlace.objects.order_by("-votos").all()
	template = "index.html"
	return render_to_response(template,locals())
@login_required
def minus(request,id_enlace):
	enlace = Enlace.objects.get(pk=id_enlace)
	enlace.votos -= 1
	enlace.save()
	return HttpResponseRedirect("/")
@login_required
def plus(request,id_enlace):
	enlace = Enlace.objects.get(pk=id_enlace)
	enlace.votos += 1
	enlace.save()
	return HttpResponseRedirect("/")

def categoria(request,id_categoria):
	categorias = Categoria.objects.all()
	cat = get_object_or_404(Categoria,pk = id_categoria)
	#cat = Categoria.objects.get(pk=id_categoria)
	enlaces = Enlace.objects.filter(categoria = cat)
	template = "index.html"
	return render_to_response(template,locals())
@login_required
def add(request):
	if request.method == "POST":
		form = EnlaceForm(request.POST)
		if form.is_valid():
			enlace = form.save(commit = False) #todavia no te guardes en la DB
			enlace.usuario = request.user
			enlace.save()
			return HttpResponseRedirect("/")
	else:
		form = EnlaceForm()
	template = "form.html"
	return render_to_response(template,context_instance = RequestContext(request,locals())) 