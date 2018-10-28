from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from vendor.forms import Custom_UserCreationForm
from django.contrib.auth import login, logout
from django.core.mail import send_mail
from django.conf import settings

from vendor.models import VendorProfile


def signup_view(request):
    if request.method == 'POST':
        form = Custom_UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            contact_number = form.cleaned_data['contact_number']
            VendorProfile.objects.create(Vendor=user, phone_number=contact_number)

            send_mail('Hello', 'Register', settings.EMAIL_HOST_USER, [user.email], fail_silently=True)
            login(request, user)
            return redirect('vendor:view_products')
    else:
        form = Custom_UserCreationForm()
    return render(request, 'Authentication/signup.html', {'form': form})


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
    return render(request, 'Authentication/login.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return render(request, 'Authentication/logout_page.html')
