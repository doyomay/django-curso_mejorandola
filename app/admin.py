from django.contrib import admin
from models import * ##aguas con los modelos que se importan

from actions import export_as_csv
# Register your models here.
class EnlaceAdmin(admin.ModelAdmin):
	list_filter = ('categoria','usuario','timestamp',)
	list_editable = ('titulo','categoria','enlace',)
	list_display = ('titulo','enlace','categoria','votos','imagen_voto','es_popular','usuario',)
	list_display_links = ('es_popular',)
	search_fields = ('categoria__titulo','enlace__titulo','usuario__username',)
	raw_id_fields = ('categoria','usuario',)
	actions = [export_as_csv]
	def imagen_voto(self, obj):
		url = obj.mis_votos_en_imagen_rosada()
		tag = '<img src="%s" >' % url
		return tag
	imagen_voto.allow_tags = True
	imagen_voto.admin_order_field = 'votos'

class EnlaceInline(admin.StackedInline):
	model = Enlace
	extra = 1
	raw_id_fields = ('usuario',)

class CategoriaAdmin(admin.ModelAdmin): ##se puede llamar como quiera, por convencion se usa el del modelo asociado
	actions = [export_as_csv]
	inlines = [EnlaceInline]

class AgregadorAdmin(admin.ModelAdmin):
	filter_horizontal = ('enlaces',)

admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Enlace,EnlaceAdmin)
admin.site.register(Agregador,AgregadorAdmin)