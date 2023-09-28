"""
URL configuration for medicine_availability project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from medicine_app.views import call_view,Search_view,index,get_name,make_call

urlpatterns = [

    path('admin/', admin.site.urls),
    path('home',get_name,name='home'),
    path('call',make_call,name='call'),
    path('search',Search_view,name='call'),
    path('search-medicine',get_name,name='get_name'),
    path('make-call',make_call,name='make-call'),
]
