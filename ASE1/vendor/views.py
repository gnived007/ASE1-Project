from django.shortcuts import render, redirect
from django.http import HttpResponse
from vendor.models import Product
from vendor.forms import ProductsAdd
from django.contrib.auth.decorators import login_required


def home(request):
    return HttpResponse('Welcome to the home page!')


def index(request):
    return render(request, 'vendor/base.html')


@login_required(login_url='vendor:Authentication:login')
def add_products(request):
    form_add = ProductsAdd()
    if request.method == 'POST':
        form = ProductsAdd(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return render(request, 'vendor/add_products.html', {'form': form_add})

    return render(request, 'vendor/add_products.html', {'form': form_add})


# To display items whose qty is less than 50

def view_products(request):
    products = Product.objects.filter(qty__lte=50)
    return render(request, 'vendor/view_products.html', {'products': products})
