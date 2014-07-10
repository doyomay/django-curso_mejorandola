from django.contrib import admin
from models import *

from actions import export_as_csv
# Register your models here.
class EnlaceAdmin(admin.ModelAdmin):
	list_filter = ('categoria','usuario','timestamp',)
	list_editable = ('titulo','categoria','enlace')
	list_display = ('titulo','enlace','categoria','votos','imagen_voto','es_popular')
	list_display_links = ('es_popular',)
	search_fields = ('categoria__titulo','enlace__titulo','usuario__username')
	actions = [export_as_csv]
	def imagen_voto(self, obj):
		url = obj.mis_votos_en_imagen_rosada()
		tag = '<img src="%s" >' % url
		return tag
	imagen_voto.allow_tags = True
	imagen_voto.admin_order_field = 'votos'
admin.site.register(Categoria)
admin.site.register(Enlace,EnlaceAdmin)