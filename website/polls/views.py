from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Ola, CHEGUEI CARALHO!")
# Create your views here.