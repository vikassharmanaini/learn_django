from unicodedata import name
from django.urls import path
from my_app import views

urlpatterns = [
    path("",views.index,name="home"),
    path("about",views.about,name="about"),
    path("service",views.service,name="services"),
    path("contact",views.contact,name="contact"),

]
