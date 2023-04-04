from django.shortcuts import render
from .models import InstrumentalResearchCategory, InstrumentalResearch

# Create your views here.

# Функция сбора однотипных данных для категорий инструментальных исследований
def getting_data(instr_res_category):
    category_description = instr_res_category.description
    researches = InstrumentalResearch.objects.filter(i_r_category=instr_res_category)
    return {'category_description': category_description,
            'researches': researches,
            }


def index_view(request):
    i_r_categories = InstrumentalResearchCategory.objects.all()
    instrumental_researches = InstrumentalResearch.objects.all()
    return render(request,
                  'mainapp/index.html',
                  {'i_r_categories': i_r_categories,
                   'instrumental_researches': instrumental_researches,
                   }
           )


def instrumental_research_mrt_view(request):
    category = InstrumentalResearchCategory.objects.get(name='Магнитно-резонансная томография')
    data = getting_data(category)
    return render(request,
                  'mainapp/i_r_category.html',
                  data,
           )


def instrumental_research_kt_view(request):
    category = InstrumentalResearchCategory.objects.get(name='Компьютерная томография')
    data = getting_data(category)
    return render(request,
                  'mainapp/i_r_category.html',
                  data,
           )


def instrumental_research_rentgen_view(request):
    category = InstrumentalResearchCategory.objects.get(name='Рентгенография')
    data = getting_data(category)
    return render(request,
                  'mainapp/i_r_category.html',
                  data,
           )


def instrumental_research_uzi_view(request):
    category = InstrumentalResearchCategory.objects.get(name='Ультразвуковое исследование')
    data = getting_data(category)
    return render(request,
                  'mainapp/i_r_category.html',
                  data,
           )
