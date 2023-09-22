from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def display3(request):
    return HttpResponse("<h3> hola vista 3</h3>")

def display4(request):
    return HttpResponse("<h4> hola vista 4</h4>")