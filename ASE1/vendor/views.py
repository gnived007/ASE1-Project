from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse
from vendor.forms import ProductsAdd
from vendor.models import Category, Product


def home(request):
    return HttpResponse('Welcome to the home page!')


def index(request):
    return render(request, 'vendor/index.html')


def add_products(request):
    categories = Category.objects.all()
    form_add = ProductsAdd()
    if request.method == 'POST':
        form = ProductsAdd(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return render(request, 'vendor/add_products.html', {'form': form_add, 'categories': categories})

    return render(request, 'vendor/add_products.html', {'form': form_add, 'categories': categories})


# To display items whose qty is less than 50

def view_products(request):
    products = Product.objects.filter(qty__lte=50)
    return render(request, 'vendor/view_products.html', {'products': products})
