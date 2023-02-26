from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
     path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
      path('cart/', views.cart_detail, name='cart_detail'),
]
