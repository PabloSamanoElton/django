from django.urls import path
from apps.productos.views import index, plantilla, listado, categorias, ViewProducto, home, nuevoRegistro, editarRegistro, eliminarRegistro, prebunta, nuevoRegistroC, editarRegistroC, eliminarRegistroC, prebuntaC, listadoC

app_name = 'productos'
urlpatterns = [
	path('', index),
	path('index', index),
	path('plantilla', plantilla),
	path('categorias', categorias),
	path('idk', ViewProducto.as_view()),
	path('listado', listado, name="infoproductos"),
	path('home', home, name="home"),
	path('prebunta', prebunta, name="prebunta"),
	path('nuevoRegistro', nuevoRegistro, name="nuevoRegistro"),
	path('editarRegistro/<idProducto>', editarRegistro, name="editarRegistro"),
	path('eliminarRegistro/<idProducto>', eliminarRegistro, name="eliminarRegistro"),
	path('listadoC', listadoC, name="infocategorias"),
	path('prebuntaC', prebuntaC, name="prebuntaC"),
	path('nuevoRegistroC', nuevoRegistroC, name="nuevoRegistroC"),
	path('editarRegistroC/<idCategoria>', editarRegistroC, name="editarRegistroC"),
	path('eliminarRegistroC/<idCategoria>', eliminarRegistroC, name="eliminarRegistroC"),
]