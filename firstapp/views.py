from multiprocessing import context
from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request,'home.html',{'key':'Destination'})

def wayanad_page(request):

    return render(request,'wayanad.html')

def load_sample(request):
     return render(request,'home.html')

def load_add_page(request):
     return render(request,'add.html')

def add_num(request):
     n1=int(request.GET['num1'])
     n2=int(request.GET['num2'])
     sum=n1+n2
     return render(request,'result.html',{'result':sum})


def add_product(request):
     return render(request,'add_product.html')