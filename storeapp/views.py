from django.shortcuts import render, redirect
from .models import *
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views import View
from django.contrib.auth import authenticate, login, logout

# Create your views here.

class Homepage(LoginRequiredMixin,View):
    login_url='/login/'
    def get(self, request):
        context ={
             "allitems": Items.objects.all()
        }
        return render(request, "Home.html", context)


# Cart
class CartPage(View):
    def get(self, request):
        cartitems= Cart.objects.filter(user=request.user)
        total_price= sum(ite.items.price * ite.quantity for ite in cartitems)
        return render(request, "Cart.html", {"cartitems":cartitems, "total_price":total_price})

class Add_To_Cart(View):
    def get(self, request, id):
        item2= Items.objects.get(id=id)
        cart_item, created= Cart.objects.get_or_create(items=item2, user=request.user)
        cart_item.save()
        if not created: 
            cart_item.quantity += 1
            cart_item.save()
        return redirect('/cart/')

class Remove_From_Cart(View):
    def get(self, request, id):
        cart_item = Cart.objects.filter(items_id=id) 
        cart_item.delete()
        return redirect('/cart/')  

class Increase_Quantity(View):
    def get(self, request, id):
       item3 = get_object_or_404(Cart, items_id=id)
       item3.quantity += 1
       item3.save()
       return redirect('/cart/') 

class Decrease_Quantity(View):
    def get(self, request, id):
        item3 = get_object_or_404(Cart, items_id=id)
        item3.quantity -= 1
        if item3.quantity == 0:
            item3.quantity += 1
        item3.save()
        return redirect('/cart/')


# Orders
class Place_Order(View):
    def get(self, request):
        cart_items2  = Cart.objects.filter(user=request.user)
        totalpay = sum(ite.items.price * ite.quantity for ite in cart_items2)
        return render(request, 'Orderplace.html', {"cart_items2":cart_items2, "totalpay":totalpay}) 
    def post(self, request):
        cart_items2  = Cart.objects.filter(user=request.user)
        totalpay = sum(ite.items.price * ite.quantity for ite in cart_items2)
        order= Order.objects.create(user=request.user, totalprice=totalpay)
        cart_items2.delete()
        order.save()
        return redirect('/')            
   
# Login
class Login(View):
    def get(self, request):
        contextB = {
            "error": ""
        }     
        return render(request, "Login.html", contextB)
    def post(self, request):
        person = authenticate(username= request.POST['usrnme'], password= request.POST['psswrd'])
        if person is not None:
            login(request, person)
            return redirect('/')
        else:
            contextC = {
                "error": "Invalid Username or Password"
            }
            return render(request, "Login.html", contextC)
        
# Signup
class Signup(View):
    def get(self, request):
        contextD = {
            "error2": ""
        }        
        return render(request, "Signup.html", contextD)
    def post(self, request):
        existperson = CustomUser.objects.filter(username= request.POST['usrnme'])
        if len(existperson) > 0:
            contextE ={
                "error2": "User already exist!"
            }
            return render(request, "Signup.html", contextE)
        else:
            newperson =CustomUser(username=request.POST['usrnme'], email=request.POST['eml'])
            newperson.set_password(request.POST['psword'])
            newperson.save()
            return redirect('/login/')
            