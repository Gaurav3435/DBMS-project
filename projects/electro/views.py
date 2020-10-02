from django.shortcuts import render
from .models import Products

# Create your views here.
def index(request):

    prod_list = Products.objects.all()

    return render(request, 'index.html',{'prod_list': prod_list})