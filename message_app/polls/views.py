from django.shortcuts import render, get_object_or_404
from django.template import loader
from .models import Question, Choice
from django.urls import reverse
from django.utils import timezone


# Create your views here.


from django.http import HttpResponse, HttpResponseRedirect

def results(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request,"polls/results.html", {"question":question})

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list" : latest_question_list
    }
    return HttpResponse(template.render(context,request))

def details(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request,"polls/detail.html",{"question":question})


def new_choice(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    new_choice_text = request.POST["new_choice"]
    if(new_choice_text):
        c = Choice.objects.create(choice_text = new_choice_text,question=question)
        c.save()
        return HttpResponseRedirect(f"../../polls/{question.id}")
    else:
        return render(
            request,
            "polls/new_choice.html",
            {
                "question":question,
                "error_message" : "You did not enter a new choice"
            }
            )


def vote(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(  
            request,
            "polls/detail.html",
            {
                "question":question,
                "error_message" : "You did not select a choice"
            }
        )
    else:
        selected_choice.votes+=1;
        selected_choice.save();
        
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
    

def choices(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(
                request,
                "polls/new_choice.html",
                {
                    "question":question
                })


def new_question(request):
    try:
        question = Question.objects.create(question_text = request.POST["new_question"],pub_date=timezone.now())
        question.save()
        return HttpResponseRedirect(reverse("polls:",args=(question.id,)))
    except:
        latest_question_list = Question.objects.order_by("-pub_date")[:5]
        return render(request,
                      "polls/index.html",
                      {
                          "latest_question_list":latest_question_list
                      })