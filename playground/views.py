from django.shortcuts import render
from store.models import Product,OrderItem,Order
# Create your views here.

def  say_hello(request):

    return render(request,'hello.html',{'name':'kiarash','products':list(queryset)})