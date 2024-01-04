from django.urls import path

from . import views


urlpatterns = [
    path("index/",views.index, name="index"),
    
    path("<int:question_id>/",views.details, name="details"),
    
    path("<int:question_id>/results/",views.results,name="result"),
    
    path("<int:question_id>/vote",views.vote,name="vote"),
]
