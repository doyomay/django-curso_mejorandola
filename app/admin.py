from django.contrib import admin
from models import *

# Register your models here.
class EnlaceAdmin(admin.ModelAdmin):
	list_display = ('titulo','enlace','categoria','votos','imagen_voto')
	list_filter = ('categoria','usuario','timestamp',)
	search_fields = ('categoria__titulo','enlace__titulo','usuario__username')
	def imagen_voto(self, obj):
		url = obj.mis_votos_en_imagen_rosada()
		tag = '<img src="%s">' % url
		return tag
	imagen_voto.allow_tags = True
admin.site.register(Categoria)
admin.site.register(Enlace,EnlaceAdmin)