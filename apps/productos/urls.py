from django.urls import path
from apps.productos.views import index, listado, categorias, ViewProducto, home, nuevoRegistro, editarRegistro, eliminarRegistro, prebunta, nuevoRegistroC, editarRegistroC, eliminarRegistroC, prebuntaC, listadoC, comprar, prueba, Ventas, ventaFormulario, ErrorCantidad

app_name = 'productos'
urlpatterns = [
	path('', index),
	path('index', index),
	path('producto/index', index),
	path('categorias', categorias),

	path('idk', ViewProducto.as_view()),
	path('home', home, name="home"),

	path('prueba', prueba, name="prueba"),

	path('ErrorCantidad', ErrorCantidad, name="ErrorCantidad"),
	path('ventaProducto/<idProducto>', ventaFormulario, name="ventasFormulario"),

	path('listado', listado, name="infoproductos"),
	path('prebunta/<idProducto>', prebunta, name="prebunta"),
	path('nuevoRegistro', nuevoRegistro, name="nuevoRegistro"),
	path('editarRegistro/<idProducto>', editarRegistro, name="editarRegistro"),
	path('eliminarRegistro/<idProducto>', eliminarRegistro, name="eliminarRegistro"),

	path('comprar', comprar, name="comprar"),

	path('listadoC', categorias, name="infocategorias"),
	path('prebuntaC/<idCategoria>', prebuntaC, name="prebuntaC"),
	path('nuevoRegistroC', nuevoRegistroC, name="nuevoRegistroC"),
	path('editarRegistroC/<idCategoria>', editarRegistroC, name="editarRegistroC"),
	path('eliminarRegistroC/<idCategoria>', eliminarRegistroC, name="eliminarRegistroC"),
]