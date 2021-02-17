from django.urls import path
from helloWorld import views

urlpatterns = [
    path("", views.home, name="home"),
]