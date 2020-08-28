from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm
from services.models import Service


def home_page(request):
    qs = Service.objects.all()
    context = {"title": "Home", "services_list": qs}
    return render(request, "home.html", context)


def contact_page(request):
    form  = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm()
    context = {"title": "Contact us", "form": form}
    return render(request, "contact.html", context)