from django.shortcuts import render, redirect
from django.http import HttpResponse
from vendor.models import Product, Category
from vendor.forms import ProductsAdd
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('vendor:view_products')
    else:
        form = UserCreationForm()
    return render(request, 'vendor/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('vendor:view_products')
    else:
        form = AuthenticationForm
    return render(request, 'vendor/login.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def home(request):
    return HttpResponse('Welcome to the home page!')


def index(request):
    return render(request, 'vendor/index.html')


@login_required(login_url='vendor:login')
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
