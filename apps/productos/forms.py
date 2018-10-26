from django import forms
from apps.productos.models import Producto, Categoria

class ProductoForm(forms.ModelForm):

	class Meta:

		model = Producto

		fields = [
			'Nombre',
			'Descripcion',
			'Costo',
			'Disponible',
			'NumExistencia',
			'Categoria',
		]

		labels = {
			'Nombre' : 'Nombre',
			'Descripcion' : 'Descripcion',
			'Costo' : 'Costo',
			'Disponible' : 'Disponibilidad',
			'NumExistencia' : 'Cantidad en Existencia',
			'Categoria' : 'Categoria',
		}

		widgets = {
			'Nombre' : forms.TextInput(attrs ={'class':'form-control'}),
			'Descripcion' : forms.TextInput(attrs ={'class':'form-control'}),
			'Costo' : forms.TextInput(attrs ={'class':'form-control'}),
			'Disponible' : forms.TextInput(attrs ={'class':'form-control'}),
			'NumExistencia' : forms.TextInput(attrs ={'class':'form-control'}),
			'Categoria' : forms.TextInput(attrs ={'class':'form-control'}),
		}

class CategoriaForm(forms.ModelForm):

	class Meta:

		model = Categoria

		fields = [
			'NombreCat',
			'FechaCreacion',
		]

		labels = {
			'NombreCat' : 'Nombre Categoria',
			'FechaCreacion' : 'Fecha de Creacion',
		}

		widgets = {
			'NombreCat' : forms.TextInput(attrs ={'class':'form-control'}),
			'FechaCreacion' : forms.TextInput(attrs ={'class':'form-control'}),
		}