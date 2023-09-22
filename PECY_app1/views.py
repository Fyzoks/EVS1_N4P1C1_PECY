from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def  display1(request):
    return HttpResponse("<h1>hola vista 1 </h1>")

def display2(request):
    return HttpResponse("<h2>hola vista 2 </h1>")