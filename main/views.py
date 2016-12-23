from django.shortcuts import render
from main.models import ProductMatEgo

def home(request):
	products = ProductMatEgo.objects.all()
	context = {'products': products}
	return render(request, 'home.html', context)

def product(request, id):
	product = ProductMatEgo.objects.get(id=id)
	context = {'product':product}
	return render(request, 'product.html', context)



