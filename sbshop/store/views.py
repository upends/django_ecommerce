from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
from django.contrib.auth.decorators import login_required
from .models import Cart, Product
from decimal import Decimal


# Create your views here.
def home(request):
    products = Product.objects.all()
    print(products)
    context = {
        "products" : products,
        "image_name" : 'images/spider_man.jpg'
    }
    return render(request, 'home.html', context=context)

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {'product': product}
    return render(request, 'product_detail.html', context)


def add_to_cart(request, product_id):
    if request.user.is_authenticated:
        # Get the product object
        product = Product.objects.get(id=product_id)

        # Check if a cart object exists for the user
        if 'cart_id' in request.session:
            print("CART PRESENT")
            cart_id = request.session['cart_id']
            cart = Cart.objects.get(id=cart_id)
        else:
            # Create a new cart object for the user
            cart = Cart.objects.create(user_id = request.user.id)
            request.session['cart_id'] = cart.id

        # Add the product to the cart
        cart.items.add(product)
        subtotal = cart.subtotal
        subtotal += Decimal(product.price)
        cart.subtotal = subtotal
        cart.save()
        return redirect('home')
    else:
        return redirect('login')


def cart_detail(request):
    if request.user.is_authenticated:
        if 'cart_id' in request.session:
            cart_id = request.session['cart_id']
            cart = Cart.objects.prefetch_related('items').get(id=cart_id)
            cart_products = cart.items.all()
            return render(request, 'cart_detail.html', {'cart': cart, 'cart_products':cart_products})
        else:
            cart = Cart.objects.create(user_id = request.user.id)
            cart.save()
            print(cart.id)
            cart_products = []
            request.session['cart_id'] = cart.id
            return render(request, 'cart_detail.html', {'cart': cart, 'cart_products':cart_products})
    else:
        return redirect('login')
