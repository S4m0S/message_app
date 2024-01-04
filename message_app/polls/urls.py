from django.urls import path

from . import views


urlpatterns = [
    path("indox/",views.indox, name="indox"),
    path("index/",views.index, name="index"),
]
