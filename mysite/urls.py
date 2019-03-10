"""mysite URL Configuration

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
from django.urls import path
from polls.views import index
from polls.views import createProduto
from polls.views import updateProduto
from polls.views import deleteProduto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='url_index'),
    path('create/',createProduto,name='url_create'),
    path('update/<int:pk>/',updateProduto,name='url_update'),
    path('delete/<int:pk>/',deleteProduto,name='url_delete'),
]
