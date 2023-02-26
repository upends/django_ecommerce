
# Create your views here.
from urllib.request import Request
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .forms import NewUserForm
from .models import Address
from orders.views import createOrder
from store.models import Cart

def signupRequest(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = NewUserForm()
    return render(request, 'signup.html', {'form': form})


def loginRequest(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                return HttpResponse("Invalid password")
        else:
            return HttpResponse("Invalid username or password.")
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def userAccount(request):
    if request.user.is_authenticated:
        userData = {}
        userData['first_name'] = request.user.first_name
        userData['last_name'] = request.user.last_name
        userData['email'] = request.user.email
        userData['username'] = request.user.username
        return render(request, 'account.html', {'userdata' : userData})
    else:
        return redirect('/user/login')


def logoutRequest(request):
    if request.user.is_authenticated:   
        logout(request)
        return redirect('login')
    return redirect('login')


def address(request):
    if request.user.is_authenticated:
        addresses = Address.objects.filter(user=request.user)
        if request.method == 'POST':
            user = request.user
            cart_id = request.session['cart_id']
            cart = Cart.objects.get(id=cart_id)
            choosenAddress = Address.objects.get(id=int(request.POST['address']))
            createOrder(user, cart, choosenAddress)
            del request.session['cart_id']   
            return redirect('order_success')         
        return render(request, 'viewAddress.html', {'addresses':addresses})
    return redirect('login')


def addNewAddress(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            requestBody = request.POST
            fullName = requestBody['first_name']
            contactNo = requestBody['contact_no']
            addressLine = requestBody['address']
            city = requestBody['city']
            state = requestBody['state']
            zipCode = requestBody['zip_code']
            country = requestBody['country']
            
            # saving new address
            address = Address()
            address.user = request.user
            address.full_name = fullName
            address.contact_no = contactNo
            address.address_line = addressLine
            address.city = city
            address.state = state
            address.zip_code = zipCode
            address.country = country
            address.save()
            return redirect('selectAddress')
        return render(request, 'addNewAddress.html')
    return redirect('login')
