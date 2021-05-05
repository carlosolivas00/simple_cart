from django.urls import path
from django.contrib.auth import views as auth_views
from webshop import views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='webshop/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='webshop/logout.html'), name='logout'),
    path('home/', views.home_view, name='home'),
    path('<int:pk>/product/', views.product_view, name="product"),
    path('create/', views.product_create_view, name="product-create"),
    path('cart/', views.cart_view, name="cart"),
    path('add_to_cart/', views.add_to_cart_view, name="add_to_cart"),
    path('<int:pk>/remove_from_cart/', views.remove_from_cart_view, name="remove_from_cart"),
    path('filter/', views.filter_view, name="filter"),
]