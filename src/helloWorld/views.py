from django.http import HttpResponse
from django.shortcuts import render
from .forms import StateForm


def home(request):
    context = {'form': StateForm()}
    if request.GET:
        temp = request.GET['state_name']
        print(temp)
    return render(request, "home.html", context)