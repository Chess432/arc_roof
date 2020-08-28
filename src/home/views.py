from django.shortcuts import render
from services.models import Service
from .models import HomeModel

def home_page(request):
    qs = Service.objects.all()
    qs_home = HomeModel.objects.all()
    print(qs_home)
    template_name = 'home.html'
    context = {"title": "Home", "services_list": qs, "slider": qs_home}
    return render(request, template_name, context)
