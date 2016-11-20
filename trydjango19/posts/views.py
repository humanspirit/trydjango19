from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.


def post_create(request):
    return HttpResponse("<h1>Hello Create </h1>")

def post_detail(request):
    return HttpResponse("<h1>Hello Detail </h1>")

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
