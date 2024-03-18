from django.shortcuts import render
from django.http import HttpRequest

def index(request):
    return HttpRequest("Ola, CHEGUEI CARALHO!")
# Create your views here.
