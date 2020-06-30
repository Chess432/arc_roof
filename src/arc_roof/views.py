from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    context = {"title": "Home"}
    return render(request, "home.html", context)



def about_page(request):
    context = {"title": "About us"}
    return render(request, "about.html", context)



def services_page(request):
    context = {"title": "Services"}
    return render(request, "services.html", context)


def contact_page(request):
    context = {"title": "Contact us"}
    return render(request, "contact.html", context)