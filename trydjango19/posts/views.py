
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm

# Create your views here.


def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit = False)
        instance.save()
        messages.success(request, "Succesfully created")
        return HttpResponseRedirect(instance.get_absolute_url())       
    context = {
        "form":form,
    }
    return render(request, "post_form.html", context)

def post_detail(request, id=None):
    #instance = Post.objects.get(id=3)
    instance = get_object_or_404(Post, id=id)
    context = {
        "title" : "Detail",
        "instance" : instance
    }
    return render(request, "post_detail.html", context)

def post_list(request):
    queryset = Post.objects.all()
    if request.user.is_authenticated():
        context = {
            "title": "My List",
            "object_list" : queryset
        }
    else:
        context = {
            "title": "List"
        }
    return render(request, "post_list.html", context)


def post_update(request, id = None):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance = instance)
    if form.is_valid():
        instance = form.save(commit = False)
        instance.save()
        messages.success(request, "<a href='#'>Item</a> Saved", extra_tags = 'html_safe')
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "title" : "Detail",
        "instance" : instance,
        "form":form,
    }
    return render(request, "post_form.html", context)

def post_delete(request, id = None):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, "Succesfully deleted")
    return redirect("posts:list")
