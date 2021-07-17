from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index-page'),
    path('login/',views.login, name='login'),
    path('my-account', views.myAccount, name='my-account'),
    path('product-detail', views.productDetail, name='product-detail'),
    path('product-list', views.productList, name='product-list'),
    path('wishlist', views.wishlist, name='wishlist'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
    path('contact', views.contact, name='contact'),

]
