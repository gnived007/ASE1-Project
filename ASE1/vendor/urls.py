from django.urls import path, include
from vendor import views

app_name = 'vendor'

urlpatterns = [
    path('add/', views.add_products, name='add_products'),
    path('view/', views.view_products, name='view_products'),
    path('', include('Authentication.urls')),
]
