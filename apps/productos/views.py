from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from apps.productos.models import Producto, Categoria
from apps.productos.forms import ProductoForm, CategoriaForm, VentasForm

def prueba(request):
	return HttpResponse("le")

def home(request):
	return render(request, 'home/index.html')

def index(request):
	return HttpResponse("Esta es la respuesta")

def listado(request):
	contexto = {
		'productos': Producto.objects.all()
	}
	return render(request, 'productos/infoproductos.html', contexto)

def comprar(request):
	contexto = {
		'productos': Producto.objects.all()
	}
	return render(request, 'productos/infoVentas.html', contexto)

def listadoC(request):
	contexto = {
		'categorias': Categoria.objects.all()
	}
	return render(request, 'productosCategoria/infocategorias.html', contexto)

def categorias(request):
	contexto = {
		'Categorias': Categoria.objects.all()
	}
	return render(request, 'productosCategoria/paginaCategoria.html', contexto)

def nuevoRegistro(request):
	if request.method == 'POST':
		form = ProductoForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('productos:infoproductos')
	else:
		form = ProductoForm()
	return render(request, 'productos/productoFormulario.html', {'form' : form})

def editarRegistro(request, idProducto):
	producto = Producto.objects.get(id = idProducto)
	if (request.method == 'GET'):
		form = ProductoForm(instance = producto)
	else:
		form = ProductoForm(request.POST, instance=producto)
		if form.is_valid():
			form.save()
		return redirect('productos:infoproductos')
	return render(request, 'productos/productoFormulario.html', {'form' : form})

def eliminarRegistro(request, idProducto):
	producto = Producto.objects.get(id = idProducto)
	if (request.method == 'GET'):
		form = ProductoForm(instance = producto)
	else:
		form = ProductoForm(request.POST, instance=producto)
		if form.is_valid():
			producto.delete()
		return redirect('productos:infoproductos')
	return render(request, 'productos/prebunta.html', {'form' : form})

class ViewProducto(ListView):
	model = Producto
	queryset = Producto.objects.all()
	templeate_name = 'productos/infoproductos.html'

class Ventas(ListView):
	model = Producto
	queryset = Producto.objects.all()
	templeate_name = 'productos/pagVentas.html'

def ventaFormulario(request,idProducto):
	producto = Producto.objects.get(id = idProducto)
	cant = producto.NumExistencia
	producto.NumExistencia = 0
	if (request.method == "GET"):
		form = VentasForm(instance = producto)
	else:
		form = VentasForm(request.POST, instance=producto)
		if form.is_valid():
			Costo = producto.NumExistencia
			producto.NumExistencia = cant - producto.NumExistencia
			if producto.NumExistencia < 0:
				return redirect('productos:ErrorCantidad')
			form.save()
		Costo = float(Costo) * producto.Costo
		contexto = {'Costo':Costo}
		return render(request, 'productos/pago.html', contexto)
		return redirect('productos:uarida')
	return render(request, 'productos/ventaFormulario.html', {'form' : form})

def ErrorCantidad(request):
	return render(request, 'productos/problemo.html')

def prebunta(request, idProducto):
 	return render(request, 'productos/prebunta.html')

def nuevoRegistroC(request):
	if request.method == 'POST':
		form = CategoriaForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('productosCategoria:infocategorias')
	else:
		form = CategoriaForm()
	return render(request, 'productosCategoria/categoriaFormulario.html', {'form' : form})

def editarRegistroC(request, idCategoria):
	categoria = Categoria.objects.get(id = idCategoria)
	if (request.method == 'GET'):
		form = CategoriaForm(instance = categoria)
	else:
		form = CategoriaForm(request.POST, instance = categoria)
		if form.is_valid():
			form.save()
		return redirect('productos:infocategorias')
	return render(request, 'productosCategoria/categoriaFormulario.html', {'form' : form})

def eliminarRegistroC(request, idCategoria):
	categoria = Categoria.objects.get(id = idCategoria)
	if (request.method == 'GET'):
		form = CategoriaForm(instance = categoria)
	else:
		form = CategoriaForm(request.POST, instance = categoria)
		if form.is_valid():
			categoria.delete()
		return redirect('productos:infocategorias')
	return render(request, 'productosCategoria/prebuntaC.html', {'form' : form})

def prebuntaC(request, idCategoria):
	return render(request, 'productosCategoria/prebuntaC.html')