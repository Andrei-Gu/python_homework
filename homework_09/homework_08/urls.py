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
from mainapp.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view),
    path('success-result/', success_result_view),
    path('ir-category-list/', IRCategoryListView.as_view()),
    path('ir-category-create/', IRCategoryCreateView.as_view()),
    path('instr-research-create/', InstrumentalResearchCreateView.as_view()),
    path(
        'ir-category/',
        include(
            [
                # В следующих URL в качестве pk подразумевается id категории инструментального исследования
                path('<int:pk>/update/', IRCategoryUpdateView.as_view()),
                path('<int:pk>/delete/', IRCategoryDeleteView.as_view()),

                # Во всех URL ниже в качестве pk подразумевается id именно конкретного инструментального исследования.
                # В случае необходимости, через него потом происходит получение объекта "Карточка"
                path('<slug:slug>/', SpecificIRCategoryListView.as_view()),
                path('<slug:short_name>/<int:pk>/', InstrumentalResearchDetailView.as_view()),
                path('<slug:short_name>/<int:pk>/update/', InstrumentalResearchUpdateView.as_view()),
                path('<slug:short_name>/<int:pk>/delete/', InstrumentalResearchDeleteView.as_view()),
                path('<slug:short_name>/<int:pk>/card-create/', InstrumentalResearchCardCreateView.as_view()),
                path('<slug:short_name>/<int:pk>/card-update/', InstrumentalResearchCardUpdateView.as_view()),
                path('<slug:short_name>/<int:pk>/card-delete/', InstrumentalResearchCardDeleteView.as_view()),
            ]
        )
    ),
]
