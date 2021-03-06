"""trydjango19 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from .views import (
    post_create,
    post_detail,
    post_list,
    post_delete,
    post_update,
)

urlpatterns = [
    url(r'^create/$',post_create),
    url(r'^(?P<id>\d+)/$',post_detail, name = 'detail'),
    url(r'^list/$',post_list, name = "list"),
    url(r'^(?P<id>\d+)/delete/$',post_delete),
    url(r'^(?P<id>\d+)/edit/$',post_update, name= 'update'),

]
