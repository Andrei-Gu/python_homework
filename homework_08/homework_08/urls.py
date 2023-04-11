"""homework_08 URL Configuration

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
from django.urls import include, path
from mainapp.views import index_view, IRCategoryListView, KTView, MRTView, UZIView, ResearchDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view),
    path('ir-category-list/', IRCategoryListView.as_view(template_name='mainapp/ir-category-list.html')),
    path(
        'ir-category/',
        include(
            [
                path('kt/', KTView.as_view(template_name='mainapp/instr-research-list.html')),
                path('kt/<int:pk>/', ResearchDetailView.as_view(template_name='mainapp/research-detail.html')),
                path('mrt/', MRTView.as_view(template_name='mainapp/instr-research-list.html')),
                path('mrt/<int:pk>/', ResearchDetailView.as_view(template_name='mainapp/research-detail.html')),
                path('uzi/', UZIView.as_view(template_name='mainapp/instr-research-list.html')),
                path('uzi/<int:pk>/', ResearchDetailView.as_view(template_name='mainapp/research-detail.html')),
            ]
        )
    ),
]
