from django.urls import path
from . import views

urlpatterns = [
    path('view_order/', views.viewOrderDetials, name='view_order'),
    path('order/<int:order_id>/', views.order_detail, name='order_detail'),
    path('order_success', views.orderSuccess, name='order_success')
]