import re
from django.shortcuts import redirect, render
from .models import Order
from django.http import HttpResponse
from store.models import Cart

# Create your views here.
def createOrder(user, cart, address):
    order = Order.objects.create(user=user, cart=cart, address=address, total_price=cart.subtotal, payment_method='test', status='processing')
    


def viewOrderDetials(request):
    if request.user.is_authenticated:
        orders = Order.objects.filter(user = request.user).order_by('-id')
        return render(request, 'orderView.html', {'orders':orders})
    else:
        return redirect('login')


def order_detail(request, order_id):
    order = Order.objects.get(id=order_id)
    cart = Cart.objects.prefetch_related('items').get(id=order.cart.id)
    order_items = cart.items.all()
    return render(request, 'orderDetail.html', {'order':order, 'order_items':order_items})


def orderSuccess(request):
    if request.user.is_authenticated:
        return render(request, 'orderSuccess.html')
    return redirect('login')