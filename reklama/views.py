from django.shortcuts import render
from .models import Product, Category
from django.db.models import Q
from django.http import HttpResponse
# Create your views here.


def index(request):
    
    gozleg = request.GET.get('search')
    if gozleg:
        products = Product.objects.filter(Q(name__icontains=gozleg) | Q(discription__icontains=gozleg))
        return render(request,'reklama.html',{'products':products})
    products = Product.objects.all()
    return render(request,'reklama.html',{'products':products})

def elekrtonika(request):
    catagory_ady='Elektronics'

    gozleg = request.GET.get('search')
    if gozleg:
        products = Product.objects.filter(Q(name__icontains=gozleg) | Q(discription__icontains=gozleg))
        return render(request,'reklama.html',{'products':products})


    category = Category.objects.get(name=catagory_ady)
    products = Product.objects.filter(Category=category)
    return render(request,'elektronika.html',{'products':products})



def basgalar(request):
    catagory_ady='Basgalar'

    gozleg = request.GET.get('search')
    if gozleg:
        products = Product.objects.filter(Q(name__icontains=gozleg) | Q(discription__icontains=gozleg))
        return render(request,'reklama.html',{'products':products})


    category = Category.objects.get(name=catagory_ady)
    products = Product.objects.filter(Category=category)
    return render(request,'elektronika.html',{'products':products})


def details(request,slug):

    product = Product.objects.get(slug=slug)
    return render (request, 'details.html',{'product':product})