from django.urls import path, re_path
from vendor import views

urlpatterns = [
    path('add/', views.add_products, name='add_products'),
    path('view/', views.view_products, name='view_products'),
]
