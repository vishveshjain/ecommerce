from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def productDetail(request):
    return render(request,'product-detail.html')

def productList(request):
    return render(request,'product-list.html')

def login(request):
    return render(request,'login.html')

def myAccount(request):
    return render(request,'my-account.html')

def contact(request):
    return render(request, 'contact.html')

def checkout(request):
    return render(request, 'checkout.html')

def cart(request):
    return render(request, 'cart.html')

def wishlist(request):
    return render(request, 'wishlist.html')