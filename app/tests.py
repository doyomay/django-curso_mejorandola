from django.test import TestCase
from .models import Categoria,Enlace

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class SimpleTest(TestCase):	
	##sencilla prueba a modelos
	def setUp(self):
		self.categoria = Categoria.objects.create(titulo='Categoria de prueba')
		self.usuario = User.objects.create_user(username='yeyo', password='ppsspp')

	def test_es_popular(self):
		enlace = Enlace.objects.create(titulo='Prueba',enlace='http://facebool.com',
			votos=0,categoria=self.categoria,usuario=self.usuario)
		# si un enlace tiene menos de 11 votos no es popupar
		self.assertEqual(enlace.votos,0)
		self.assertEqual(enlace.es_popular(),False)
		self.assertFalse(enlace.es_popular())

		enlace.votos = 20
		enlace.save()

		# si un enlace tiene mas de 11 votos es popupar
		#self.assertEqual(enlace.votos,0)
		self.assertEqual(enlace.es_popular(),True)
		self.assertTrue(enlace.es_popular())
		##Prueba a vistas si existen o no
	def test_views(self):
		res = self.client.get(reverse('index'))
		self.assertEqual(res.status_code, 200)

		res = self.client.get(reverse('about'))
		self.assertEqual(res.status_code, 200)

		res = self.client.get(reverse('enlaces'))
		self.assertEqual(res.status_code, 200)

		self.assertTrue(self.client.login(username='yeyo',password='ppsspp'))

		res = self.client.get(reverse('add'))
		self.assertEqual(res.status_code, 200)
	
	def test_add(self):
		self.assertTrue(self.client.login(username='yeyo',password='ppsspp'))##verrificamos que este logueado correctamente
		self.assertEqual(Enlace.objects.count(),0)
		data = {}
		data['titulo'] = 'titulo'
		data['enlace'] = 'http://facebook.com/' ##tener en cuenta que django valida enlaces y el los pone como debe de ser
		data['categoria'] = self.categoria.id
		res = self.client.post(reverse('add'),data)
		self.assertEqual(res.status_code,302)
		self.assertEqual(Enlace.objects.count(),1)

		enlace = Enlace.objects.all()[0]
		self.assertEqual(enlace.titulo, data['titulo'])
		self.assertEqual(enlace.enlace, data['enlace'])
		self.assertEqual(enlace.categoria,self.categoria)