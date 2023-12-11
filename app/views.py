from urllib.request import Request
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from .models import Customer,Product,Cart,OrderPlaced
from .forms import CustomerRegistrationForm
from django.contrib import messages
from django.contrib.auth import logout

class ProductView(View):
    def get(self,request):
        topwears=Product.objects.filter(category='TW')
        buttomwears=Product.objects.filter(category='BW')
        mobiles=Product.objects.filter(category='M')
        return render(request,'app/home.html',{'topwears':topwears,'buttomwears':buttomwears,'mobiles':mobiles})


"""def product_detail(request):
 return render(request, 'app/productdetail.html')"""

class ProductDetailView(View):
    def get(self,request,pk):
        product=Product.objects.get(pk=pk)
        return render(request,'app/productdetail.html',{'product':product})

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def mobile(request,data=None):
    if data==None:
        mobiles=Product.objects.filter(category='M')
    if data=="Apple" or data=="SAMSUNG" or data=="ONEPLUS":
        mobiles=Product.objects.filter(category="M").filter(brand=data)
    if data=='below':
        mobiles=Product.objects.filter(category='M').filter(discounted_price__lt=60000)
    if data=='above':
        mobiles=Product.objects.filter(category='M').filter(discounted_price__gt=60000)
    return render(request, 'app/mobile.html',{"mobiles":mobiles})

def topwear(request,data=None):
    if data==None:
        topwears=Product.objects.filter(category='TW')
    if data=='below':
         topwears=Product.objects.filter(category='TW').filter(discounted_price__lt=400)
    if data=='above':
         topwears=Product.objects.filter(category='TW').filter(discounted_price__gt=400)
    return render(request, 'app/topwear.html',{"topwears":topwears})

def buttomwear(request,data=None):
    if data==None:
        buttomwear=Product.objects.filter(category='BW')
    if data=='below':
       buttomwear=Product.objects.filter(category='BW').filter(discounted_price__lt=500)
    if data=='above':
       buttomwear=Product.objects.filter(category='BW').filter(discounted_price__gt=500)
    return render(request, 'app/buttomwear.html',{"buttomwear":buttomwear})

def login(request):
 return render(request, 'app/login.html')

class CustomerRegistrationView(View):
    def get(self,request):
        form=CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html',{'form':form})
    
    def post(self,request):
        form=CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            form=CustomerRegistrationForm()
            messages.success(request,'HURRAY SIGNED_UP SUCCESSFULLY !!')
            
        return render(request, 'app/customerregistration.html',{'form':form})
    
def checkout(request):
 return render(request, 'app/checkout.html')
