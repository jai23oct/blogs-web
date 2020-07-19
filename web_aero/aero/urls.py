"""stab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from gallery import urls as gallery_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^gallery/', include(gallery_urls))
"""
from django.conf.urls import url,include
from . import views
from django.views.generic import ListView, DetailView

from django.urls import path

urlpatterns = [
    url(r'^$',views.revamp,name='revamp'),
    url(r'events/$',views.events ,name='events'),
    url(r'gallery/$',views.gallery ,name='gallery'),
    url(r'addblogs/$',views.addblogs, name='addblogs'),
    url(r'blogs/$',views.blogs, name='blogs'),
    path('blogs/<int:pk>/',views.gblog, name='gblog'),
    
]

