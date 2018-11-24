from django.db import models

class Categoria(models.Model):
	NombreCat = models.CharField(max_length=30)
	FechaCreacion = models.DateField(default = '2000-01-01')

	def __str__(self):
		return '{}'.format(self.NombreCat)

class Producto(models.Model):
	Nombre = models.CharField(max_length=30)
	Descripcion = models.CharField(max_length=30)
	Costo = models.IntegerField(default = 0)
	Disponible = models.BooleanField(default = 0)
	NumExistencia = models.IntegerField(default = 1)
	Categoria = models.ForeignKey(Categoria, null=True, blank = True, on_delete = models.CASCADE)
	# wtf is this
	def __str__(self):
		return '{}'.format(self.id)