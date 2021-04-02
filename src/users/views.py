from django.shortcuts import render
from .forms import UserForm
from .models import User


def user_create_view(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = UserForm()

    context = {
        'form': form
    }
    return render(request, "user/user_create.html", context)


def user_detail_view(request):
    obj = User.objects.get(id=2)
    context = {
        'object': obj
    }
    return render(request, "user/user_detail.html", context)