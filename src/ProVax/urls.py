"""ProVax URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from users.views import user_detail_view, user_create_view, user_good_view, user_not_view
from pages.views import home_view, about_view

urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),  # Django admin site
    path('user/', user_detail_view),  # Access user input
    path('eligibility/', user_create_view),  # The vaccine eligibility survey page
    path('home/', home_view),  # The ProVax home page
    path('about/', about_view),  # About the authors
    path('eligible/', user_good_view),  # Landing page for eligible users
    path('ineligible/', user_not_view),  # Landing page for ineligible users
]
