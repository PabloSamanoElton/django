from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from apps.productos.models import Producto, Categoria
from apps.productos.forms import ProductoForm, CategoriaForm

def index(request):
	return HttpResponse("Esta es la respuesta")

def plantilla(request):
	return render(request, 'productos/index.html')

def listado(request):
	contexto = {
		'productos': Producto.objects.all()
	}
	return render(request, 'productos/infoproductos.html', contexto)

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
		form = ProductoForm(instance = Producto)
	else:
		form = ProductoForm(request.POST, instance=Producto)
		if form.is_valid():
			form.save()
		return redirect('productos:infoproductos')
	return render(request, 'productos/productoFormulario.html', {'form' : form})

def eliminarRegistro(request, idProducto):
	producto = Producto.objects.get(id = idProducto)
	if (request.method == 'GET'):
		form = ProductoForm(instance = Producto)
	else:
		form = ProductoForm(request.POST, instance=Producto)
		if form.is_valid():
			producto.delete()
		return redirect('productos:infoproductos')
	return render(request, 'productos/prebunta.html'), {'form' : form}


class ViewProducto(ListView):
	model = Producto
	queryset = Producto.objects.all()
	templeate_name = 'productos/infoproductos.html'

def home(request):
	return render(request, 'home/index.html')

def prebunta(request):
 	return render(request, 'productos/prebunta.html')

def nuevoRegistroC(request):
	if request.method == 'POST':
		form = CategoriaForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('productosCateogira:infocategorias')
	else:
		form = CategoriaForm()
	return render(request, 'productosCateogira/categoriaFormulario.html', {'form' : form})

def editarRegistroC(request, idCategoria):
	categoria = Categoria.objects.get(id = idCategoria)
	if (request.method == 'GET'):
		form = CategoriaForm(instance = Categoria)
	else:
		form = CategoriaForm(request.POST, instance=Categoria)
		if form.is_valid():
			form.save()
		return redirect('productos:infocategorias')
	return render(request, 'productosCateogira/categoriaFormulario.html', {'form' : form})

def eliminarRegistroC(request, idCategoria):
	categoria = Categoria.objects.get(id = idCategoria)
	if (request.method == 'GET'):
		form = CategoriaForm(instance = Categoria)
	else:
		form = CategoriaForm(request.POST, instance=Categoria)
		if form.is_valid():
			categoria.delete()
		return redirect('productos:infocategorias')
	return render(request, 'productosCateogira/prebuntaC.html', {'form' : form})

def prebuntaC(request):
	return render(request, 'productosCateogira/prebuntaC.html')