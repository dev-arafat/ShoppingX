from urllib import request

from app import views
from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .forms import CoustomerProfile
from .models import Customer, Product, Cart, OrderPlaced
from .models import *


#def home(request):
 #return render(request, 'app/home.html')

class ProductView(View):
 def get(self, request):
  topwears = Product.objects.filter(category='TW')
  bottomwears = Product.objects.filter(category='BW')
  mobiles = Product.objects.filter(category='M')
  laptop = Product.objects.filter(category='l')
  return render(request, 'app/home.html', {'topwears': topwears, 'bottomwears': bottomwears, 'mobiles': mobiles, 'laptop': laptop})

#def product_detail(request):
 #return render(request, 'app/productdetail.html')


class ProductDetailView(View):
 def get(self, request, pk):
  product = Product.objects.get(pk=pk)
  return render(request, 'app/productdetail.html', {'product': product})



def add_to_cart(request):
 return render(request, 'app/addtocart.html')


def buy_now(request):
 return render(request, 'app/buynow.html')


def search(request):
    if request.method == "GET":
        name = request.GET.get("searchvalue")
        prod = Product.objects.filter(title__startswith=name)
        print(prod)
        return render(request, "app/search.html", {"product": prod})
    return render(request, 'app/search.html')


#def profile(request):
 #return render(request, 'app/profile.html')


def address(request):
    add = Customer.objects.filter(user=request.user)
    return render(request, 'app/address.html',{'add':add, 'active':'btn-primary'})

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request, data=None):
 if data == None:
  mobiles = Product.objects.filter(category='M')
 return render(request, 'app/mobile.html', {'mobiles': mobiles})


def laptop(request, data=None):
 if data == None:
  laptops = Product.objects.filter(category='l')
 return render(request, 'app/laptop.html', {'laptops': laptops})


def login(request):
 if request.method == 'POST':
  username = request.POST['username']
  password = request.POST['password']
  user = auth.authenticate(username=username, password=password)
  if user is not None:
   auth.login(request, user)
   return redirect('home')
  else:
   messages.error(request, 'password not match')
   return redirect('customerregistration')
 return render(request, 'app/login.html')

def customerregistration(request):
 if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exist')
            elif User.objects.filter(email = email).exists():
                messages.error(request, 'Email already exist')
            else:
               user=User.objects.create_user(username=username, password=password, email=email)
               user.save();
               return redirect('login')
        else:
            messages.error(request,'password & password1 not matched')
 return render(request, 'app/customerregistration.html')

def checkout(request):
 return render(request, 'app/checkout.html')

class ProfileView(View):
    def get(self, request):
        form = CoustomerProfile()
        return render(request, 'app/profile.html', {'form': form, 'active':'btn-primary'})
    def post(self, request):
        form = CoustomerProfile(request.POST)
        if form.is_valid():
            usr = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipCode = form.cleaned_data['zipCode']
            reg =Customer(user=usr, name=name, locality=locality, city=city, state=state, zipCode=zipCode)
            reg.save()
            messages.success(request, 'Congratulations Profile Updated Successfully')
        return render(request, 'app/profile.html', {'form': form, 'active':'btn-primary'})
