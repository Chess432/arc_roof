from django.shortcuts import render
from .models import Service
from django.shortcuts import render, get_object_or_404, redirect



def services_list_view(request):
    qs = Service.objects.all()
    template_name = 'services/list.html'
    context = {"title": "Services", "services_list": qs}
    return render(request, template_name, context)


def services_detail_view(request, slug):
    obj = get_object_or_404(Service, slug=slug)
    template_name = "services/detail.html"
    context = {"object": obj, "title": obj.title}
    return render(request, template_name,context)

