from django.urls import path, re_path
from vendor import views

app_name = 'vendor'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('add/', views.add_products, name='add_products'),
    path('view/', views.view_products, name='view_products'),
]
