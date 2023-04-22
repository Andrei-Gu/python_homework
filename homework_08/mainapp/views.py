from django.shortcuts import render
from .models import InstrumentalResearchCategory, InstrumentalResearch, InstrumentalResearchCard, Preparation
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import IRCategoryForm, InstrumentalResearchForm, InstrumentalResearchCardForm


def index_view(request):
    return render(request, 'mainapp/index.html', {'content': 'Вас приветствует BestMed!'})


def success_result_view(request):
    return render(request, 'mainapp/index.html', {'content': 'Действие успешно выполнено'})


# Вью для отображения видов инструментальных исследований. Фильтрацию по полю "is_available" не делал.
class IRCategoryListView(ListView):
    model = InstrumentalResearchCategory
    template_name = 'mainapp/ir_category_list.html'


class IRCategoryCreateView(CreateView):
    model = InstrumentalResearchCategory
    template_name = 'mainapp/ir_category_form.html'
    # fields = '__all__'
    form_class = IRCategoryForm
    success_url = '/ir-category-list/'


class IRCategoryUpdateView(UpdateView):
    model = InstrumentalResearchCategory
    template_name = 'mainapp/ir_category_form.html'
    # fields = '__all__'
    form_class = IRCategoryForm
    success_url = '/ir-category-list/'


class IRCategoryDeleteView(DeleteView):
    model = InstrumentalResearchCategory
    template_name = 'mainapp/confirm_delete.html'
    success_url = '/ir-category-list/'


# Вью для отображения списка исследований конкретной категории
class SpecificIRCategoryListView(ListView):
    model = InstrumentalResearch
    template_name = 'mainapp/instr_research_list.html'

    def get_queryset(self):
        slug = self.kwargs['slug']
        instr_res_category = InstrumentalResearchCategory.objects.get(short_name=slug)
        query = InstrumentalResearch.objects.filter(i_r_category=instr_res_category)
        return query


    def get_context_data(self, **kwargs):
        # кортеж для понимания, создана ли уже карточка у конкретного исследования
        i_r_card = ()
        context = super().get_context_data(**kwargs)
        for item in context['object_list']:
            # Django не умеет делать get_or_none(), поэтому приходится получать пустой или непустой queryset по id
            if len(InstrumentalResearchCard.objects.filter(instrumental_research=item.id)) > 0:
                i_r_card += (item.id, )
        context['i_r_card'] = i_r_card
        return context


class InstrumentalResearchCreateView(CreateView):
    model = InstrumentalResearch
    template_name = 'mainapp/instr_research_form.html'
    # fields = '__all__'
    form_class = InstrumentalResearchForm
    success_url = '/success-result/'


class InstrumentalResearchUpdateView(UpdateView):
    model = InstrumentalResearch
    template_name = 'mainapp/instr_research_form.html'
    # fields = '__all__'
    form_class = InstrumentalResearchForm
    success_url = '/success-result/'


class InstrumentalResearchDeleteView(DeleteView):
    model = InstrumentalResearch
    template_name = 'mainapp/confirm_delete.html'
    success_url = '/success-result/'


# Вью для отображения информации о конкретном инструментальном исследований, например, КТ головного мозга,
# включая его название и описание, описание подготовки к исследованию, цену
class InstrumentalResearchDetailView(DetailView):
    model = InstrumentalResearch
    template_name = 'mainapp/research_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        i_r_card = InstrumentalResearchCard.objects.get(instrumental_research=self.object.id)
        i_r_preparations = Preparation.objects.filter(instrumentalresearchcard__id=i_r_card.id)
        context['i_r_card'] = i_r_card
        context['i_r_preparations'] = i_r_preparations
        return context


class InstrumentalResearchCardCreateView(CreateView):
    model = InstrumentalResearchCard
    template_name = 'mainapp/instr_research_card_form.html'
    form_class = InstrumentalResearchCardForm
    success_url = '/success-result/'

    def form_valid(self, form):
        i_r_card = form.save(commit=False)
        instrumental_research_id = self.kwargs['pk']
        i_r_card.instrumental_research = InstrumentalResearch.objects.get(id=instrumental_research_id)
        i_r_card.save()
        return super().form_valid(form)


    def get_context_data(self, **kwargs):
        # Так как объект (карточка) еще не создан, то приходится отдельно вытягивать название исследования,
        # для которого создается карточка, чтобы отображать его она странице
        context = super().get_context_data(**kwargs)
        instrumental_research_id = self.kwargs['pk']
        instrumental_research = InstrumentalResearch.objects.get(id=instrumental_research_id)
        context['i_r_name'] = instrumental_research.name
        return context


class InstrumentalResearchCardUpdateView(UpdateView):
    model = InstrumentalResearchCard
    template_name = 'mainapp/instr_research_card_form.html'
    form_class = InstrumentalResearchCardForm
    success_url = '/success-result/'

    def get_object(self, queryset=None, **kwargs):
        instrumental_research_id = self.kwargs['pk']
        return InstrumentalResearchCard.objects.get(instrumental_research=instrumental_research_id)


class InstrumentalResearchCardDeleteView(DeleteView):
    model = InstrumentalResearchCard
    template_name = 'mainapp/confirm_instr_research_card_delete.html'
    success_url = '/success-result/'

    def get_object(self, queryset=None, **kwargs):
        instrumental_research_id = self.kwargs['pk']
        return InstrumentalResearchCard.objects.get(instrumental_research=instrumental_research_id)
