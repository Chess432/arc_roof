from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from django.http import Http404
from .forms import BlogPostModelFom
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


def blog_post_list_view(request):
    qs = BlogPost.objects.all().published()
    if request.user.is_authenticated:
        my_qs = BlogPost.objects.filter(user=request.user)
        qs = (qs|my_qs).distinct()
    template_name = "blog/list.html"
    context = {"title":"Blogs - ", "object_list": qs}
    return render(request, template_name, context)


@staff_member_required
# @login_required
def blog_post_create_view(request):
    form = BlogPostModelFom(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        #obj.title = form.cleaned_data.get("title")+"0"
        obj.user = request.user
        obj.save()
        form = BlogPostModelFom()
    template_name = "blog/create.html"
    context = {"form": form, "title": "Create new Blog"}
    return render(request, template_name, context)

def blog_post_detail_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = "blog/detail.html"
    context = {"object": obj, "title": obj.title}
    return render(request, template_name, context)

@staff_member_required
def blog_post_update_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    form = BlogPostModelFom(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    template_name = "blog/create.html"
    context = {"form": form, "title": f"update {obj.title}"}
    return render(request, template_name, context)


@staff_member_required
def blog_post_delete_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = "blog/delete.html"
    if request.method == 'POST':
        obj.delete()
        return redirect("/blog")
    context = {"object": obj}
    return render(request, template_name, context)
