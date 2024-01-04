from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World !")

def details(request, question_id):
    return HttpResponse("You are looking at the question %s" % question_id)

def results(request, question_id):
    return HttpResponse("You are looking at the results of question %s" % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s" % question_id)