from django.urls import path, re_path
from vendor import views

urlpatterns = [
    path('', views.add_products, name='add_products'),
]
