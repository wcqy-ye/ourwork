"""thesale URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from django.shortcuts import HttpResponse
from django.shortcuts import render
from loginupin import views as loginupin_views
from theteam import views as theteam_views
import xadmin
import haystack

urlpatterns = [
    path('',include('loginupin.urls', namespace='loginupin')),
    path('xadmin/', xadmin.site.urls),
    path('loginupin/', include('loginupin.urls', namespace='loginupin')),
    url(r'^search/', include('haystack.urls')),
    path('thingfloat/',include('thingfloat.urls')),
    path('taskout/', include('taskout.urls')),
    path('theteam/', include('theteam.urls', namespace='theteam')) # 引入blog应用的url配置
]
