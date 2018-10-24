from django.shortcuts import render, reverse, redirect
from vendor.forms import ProductsAdd
from vendor.models import Category


def index(request):
    return render(request, 'vendor/index.html')


def add_products(request):
    categories = Category.objects.all()
    form = ProductsAdd()
    if request.method == 'POST':
        form = ProductsAdd(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return render(request, 'vendor/add_products.html', {'form': form, 'categories': categories})

    return render(request, 'vendor/add_products.html', {'form': form, 'categories': categories})
