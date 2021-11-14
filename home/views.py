from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# class HomeView(TemplateView):
#     template_name = "home.html"

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request,'about.html')

def products(request):
    return render(request,'products.html')

def hours(request):
    return render(request, 'hours.html')
