from django.shortcuts import render
from .models import  Testimonials




def about_testimonials(request):
    qs  = Testimonials.objects.all()
    template_name = 'about.html'
    context = {"about_testimonial": qs}
    return render(request, template_name, context)