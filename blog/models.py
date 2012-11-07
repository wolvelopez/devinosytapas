from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
	nombre = models.CharField(max_length=200)
	
	def __unicode__(self):
		return self.nombre



class Posts(models.Model):
	fecha = models.DateField()
	titulo = models.CharField(max_length=200)
	slug = models.CharField(max_length=200)
	contenido = models.TextField()
	autor = models.ForeignKey(User)
	categoria = models.ForeignKey(Categoria)

	def __unicode__(self):
		return self.titulo