from django.contrib import admin
from models import *

class ArchivosAdminInline(admin.StackedInline):
	model = Archivos
	extra = 1


#Esto hace que al escribir un titulo en el administrador se rellene a la misma vez el
#slug interpretando los espacios por guiones
class PostAdmin(admin.ModelAdmin):
	#Esto hace que al escribir un titulo en el administrador se rellene a la misma vez el
    #slug interpretando los espacios por guiones
	prepopulated_fields = {"slug": ("titulo",)}
	#mostrar la fecha
	date_hierarchy = "fecha"
	#agrupar los campos en el admin de la forma que queramos
	fieldsets = (
		(None, {
			'fields':(('fecha', 'titulo', 'slug'),'contenido',
			('autor','categoria','tag'))
			}),
		)
	#mostrar en la seccion de posts las columnas de  fecha , titulo y autor
	list_display = ['fecha', 'titulo', 'autor']
	#filtrado por categorias
	list_filter = ['categoria']
	#busqueda por titulo de post
	search_fields = ('titulo','contenido',)
	#adiccion de archivos adjuntos a los posts
	inlines = [ArchivosAdminInline]

	# #Agregaremos el tiny_mce para escribir en el blog
	class Media:
	 	js = ('js/tiny_mce/tiny_mce.js', 
	 		  'js/tiny_mce/TinyMCEAdmin.js',)
			  

admin.site.register(Posts, PostAdmin)
admin.site.register(Categoria)