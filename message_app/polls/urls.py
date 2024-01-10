from django.urls import path

from . import views



app_name = "polls"

urlpatterns = [
    path("index/",views.index, name="index"),
    
    path("<int:question_id>/",views.details, name="details"),
    
    path("<int:question_id>/results",views.results,name="results"),
    
    path("<int:question_id>/vote",views.vote,name="vote"),
    
    path("<int:question_id>/new_choice",views.new_choice,name="new_choice"),
    
    path("<int:question_id>/choice",views.choices,name="choice"),
    
    path("new_question/",views.new_question,name="new_question"),
    
]
