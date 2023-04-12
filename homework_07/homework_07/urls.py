"""homework_07 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from mainapp.views import index_view, instrumental_research_mrt_view, instrumental_research_kt_view, \
    instrumental_research_rentgen_view, instrumental_research_uzi_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view),
    path('categories/', index_view),
    path('categories/mrt/', instrumental_research_mrt_view),
    path('categories/kt/', instrumental_research_kt_view),
    path('categories/rentgen/', instrumental_research_rentgen_view),
    path('categories/uzi/', instrumental_research_uzi_view),
]
