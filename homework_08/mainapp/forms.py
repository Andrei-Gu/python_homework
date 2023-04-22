from django import forms
from .models import InstrumentalResearchCategory, InstrumentalResearch, InstrumentalResearchCard, Preparation


class IRCategoryForm(forms.ModelForm):

    name = forms.CharField(label='Название категории исследований',
                           widget=forms.Textarea(
                               attrs={
                                   'placeholder': 'Допускается 2000 символов',
                                   'class': 'form-control',
                               }
                           ))

    short_name = forms.CharField(label='Сокращенное название',
                                 widget=forms.TextInput(attrs={'placeholder': '3 - 5 английских букв'})
                                )

    description = forms.CharField(label='Описание',
                                  widget=forms.Textarea(
                                      attrs={
                                          'placeholder': 'Допускается 2000 символов',
                                          'class': 'form-control',
                                      }
                                  ))

    class Meta:
        model = InstrumentalResearchCategory
        # fields = '__all__'
        # fields = ('name', 'short_name')
        exclude = ('is_available', )


class InstrumentalResearchForm(forms.ModelForm):

    i_r_category = forms.ModelChoiceField(label='Категория инструментального исследования',
                                          queryset=InstrumentalResearchCategory.objects.all(),
                                          widget=forms.Select,
                                          )

    name = forms.CharField(label='Название исследования',
                           widget=forms.Textarea(
                               attrs={
                                   'placeholder': 'Допускается 100 символов',
                                   'class': 'form-control',
                               }
                           ))

    class Meta:
        model = InstrumentalResearch
        exclude = ('is_available', )


class InstrumentalResearchCardForm(forms.ModelForm):

    i_r_description = forms.CharField(label='Описание',
                                      widget=forms.Textarea(
                                          attrs={
                                              'placeholder': 'Допускается 2000 символов',
                                              'class': 'form-control',
                                          }
                                      ))

    i_r_preparation = forms.ModelMultipleChoiceField(label='Специальная подготовка',
                                                     queryset=Preparation.objects.all(),
                                                     widget=forms.SelectMultiple,
                                                     )

    i_r_price = forms.IntegerField(label='Цена исследования',
                                   widget=forms.NumberInput(
                                       attrs={
                                           'min': 1,
                                       }
                                   ))

    i_r_interesting_fact = forms.CharField(required=False,
                                           label='Интересный факт',
                                           widget=forms.Textarea(
                                               attrs={
                                                   'placeholder': '',
                                                   'class': 'form-control',
                                               }
                                           ))

    class Meta:
        model = InstrumentalResearchCard
        exclude = ('instrumental_research', )
