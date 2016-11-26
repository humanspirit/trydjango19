from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from .forms import PostForm

# Create your views here.


def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit = False)
        instance.save()
    context = {
        "form":form,
    }
    return render(request, "post_form.html", context)

def post_detail(request, id=None):
    #instance = Post.objects.get(id=3)
    instance = get_object_or_404(Post, id=id)
    content_data = {
        "title" : "Detail",
        "instance" : instance
    }
    return render(request, "post_detail.html", content_data)

def post_list(request):
    queryset = Post.objects.all()
    if request.user.is_authenticated():
        context_data = {
            "title": "My List",
            "object_list" : queryset
        }
    else:
        context_data = {
            "title": "List"
        }
    return render(request, "index.html", context_data)


def post_update(request):
    return HttpResponse("<h1>Hello Update </h1>")

def post_delete(request):
    return HttpResponse("<h1>Hello Delete </h1>")
