"""
URL configuration for visitors_control project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from users.views import index
from visitors.views import (register_visitor, visitor_info)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path(
        "",
        index,
        name="index"
    ),
    
    path(
        "registrar-visitante",
        register_visitor,
        name="register_visitor"
    ),
    
    path(
        "visitor/<int:id>/",            ## Precisamos indicar entre <> o tipo do dado que será utilizado na query da url, e qual o nome dele.
        visitor_info,
        name="visitor_info"
    )
]
