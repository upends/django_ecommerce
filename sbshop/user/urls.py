from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signupRequest, name='signup'),
    path('login/', views.loginRequest, name='login'),
    path('account/', views.userAccount, name='account'),
    path('logout/', views.logoutRequest, name='logout'),
    path('selectAddress/', views.address, name='selectAddress'),
    path('addNewAddress/', views.addNewAddress, name='addNewAddress'),
]
