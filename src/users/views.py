from django.shortcuts import render
from .forms import UserForm
from .models import User


def user_create_view(request):
    form = UserForm(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        form.save()
        form = UserForm()
        age = int(request.POST.get("age"))
        if age >= 16:
            return render(request, "user/user_good.html")
        else:
            return render(request, "user/user_not.html")
    return render(request, "user/user_create.html", context)


def user_detail_view(request):
    obj = User.objects.get(id=1)
    context = {
        'object': obj
    }
    return render(request, "user/user_detail.html", context)


def user_good_view(request):
    return render(request, "user/user_good.html")


def user_not_view(request):
    return render(request, "user/user_not.html")
