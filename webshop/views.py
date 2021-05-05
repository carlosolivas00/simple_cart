from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Cart
from .forms import ProductForm
from django.contrib import messages
from django.db.models.query_utils import Q


@login_required(login_url='login')
def home_view(request):
    template = 'webshop/home.html'
    context ={
        'products': Product.objects.all().order_by('name').order_by('price'),
        'cart_items': len(Cart.objects.filter(user=request.user.username))
    }
    return render(request, template, context)


@login_required(login_url='login')
def product_view(request, pk):
    template = 'webshop/product.html'
    context = {
        'product': Product.objects.get(pk=pk),
    }
    return render(request, template, context)


@login_required(login_url='login')
def product_create_view(request):
    form = ProductForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.instance.created_by = request.user.username
        form.save()
        # add message
        messages.success(request, 'Product has been created!')
        return redirect('home')
    context = {
        'form': form,
    }
    template = 'webshop/product_create.html'
    return render(request, template, context)


@login_required(login_url='login')
def filter_view(request):
    search = request.GET.get('filter')
    items = Product.objects.filter(Q(name__icontains=search) | Q(code__icontains=search))
    template = 'webshop/filter.html'
    context = {
        "products": items
    }
    return render(request, template, context)


@login_required(login_url='login')
def cart_view(request):
    cart = Product.objects.filter(cart__user=request.user.username).order_by('name')
    template = 'webshop/cart.html'
    context = {
        "cart": cart,
    }
    return render(request, template, context)


@login_required(login_url='login')
def add_to_cart_view(request):
    product_id = request.GET.get('product_id')
    Cart.objects.create(product_id=Product.objects.get(pk=product_id), user=request.user.username)
    template = 'webshop/add_to_cart.html'
    return render(request, template)


@login_required(login_url='login')
def remove_from_cart_view(request, pk):
    if request.method == 'POST':
        Cart.objects.filter(product_id=pk).first().delete()
        return redirect('cart')
    template = 'webshop/remove_from_cart.html'
    return render(request, template)

