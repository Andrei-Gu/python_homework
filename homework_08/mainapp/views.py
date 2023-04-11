from django.shortcuts import render
from .models import InstrumentalResearchCategory, InstrumentalResearch, InstrumentalResearchCard, Preparation
from django.views.generic import ListView, DetailView


def index_view(request):
    return render(request, 'mainapp/index.html', {'content': 'Вас приветствует BestMed!'})

# Вью для отображения видов инструментальных исследований
class IRCategoryListView(ListView):
    model = InstrumentalResearchCategory


# Вью для отображения списка конкретных КТ исследований, таких как КТ желудка, КТ головного мозга
class KTView(ListView):
    model = InstrumentalResearch

    def get_queryset(self):
        instr_res_category = InstrumentalResearchCategory.objects.get(short_name='kt')
        query = InstrumentalResearch.objects.filter(i_r_category=instr_res_category)
        return query


# Вью для отображения списка конкретных МРТ исследований, таких как МРТ шейного отдела позвоночника и т.д.
class MRTView(ListView):
    model = InstrumentalResearch

    def get_queryset(self):
        instr_res_category = InstrumentalResearchCategory.objects.get(short_name='mrt')
        query = InstrumentalResearch.objects.filter(i_r_category=instr_res_category)
        return query


# Вью для отображения списка конкретных УЗИ исследований, таких как УЗИ сосудов, УЗИ органов малого таза
class UZIView(ListView):
    model = InstrumentalResearch

    def get_queryset(self):
        instr_res_category = InstrumentalResearchCategory.objects.get(short_name='uzi')
        query = InstrumentalResearch.objects.filter(i_r_category=instr_res_category)
        return query


# Вью для отображения информации о конкретном инструментальном исследований, например, КТ головного мозга,
# включая его название и описание, описание подготовки к исследованию, цену
class ResearchDetailView(DetailView):
    model = InstrumentalResearch

    def get_context_data(self, **kwargs):
        context = {}
        if self.object:
            context["object"] = self.object
            context_object_name = self.get_context_object_name(self.object)
            if context_object_name:
                context[context_object_name] = self.object
        context.update(kwargs)
        context = super().get_context_data(**context)
        i_r_card = InstrumentalResearchCard.objects.get(instrumental_research=self.object.id)
        i_r_preparations = Preparation.objects.filter(instrumentalresearchcard__id=i_r_card.id)
        context['i_r_card'] = i_r_card
        context['i_r_preparations'] = i_r_preparations
        print(i_r_card.__dict__)
        print(i_r_preparations)
        return context
