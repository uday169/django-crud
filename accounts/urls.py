from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('customer/<str:pk>/', views.customer, name= 'customer'),
    path('create-order/<str:pk>/', views.createOrder, name='create_order'),
    path('update-order/<str:pk>/', views.updateOrder, name='update_order'),
    path('delete-order/<str:pk>/', views.deleteOrder, name='delete_order'),
]
