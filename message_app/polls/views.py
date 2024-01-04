from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse

def indox(request):
    return HttpResponse("Another one !")

def index(request):
    return HttpResponse("Hello World !")

