from django.db import models

# Create your models here.


# Вид инструментального исследования, напримре, МРТ, КТ, рентген, УЗИ
class InstrumentalResearchCategory(models.Model):
    name = models.CharField(unique=True, max_length=40)

    # Наверное, лучше использовать TextField - в этом поле в админке отображается больше текста
    description = models.TextField(max_length=2000)

    def __str__(self):
        return self.name


# Конкретное инструментальное исследование, например, рентген стопы или УЗИ сосудов
class InstrumentalResearch(models.Model):
    i_r_category = models.ForeignKey(InstrumentalResearchCategory, on_delete=models.CASCADE)
    name = models.CharField(unique=True, max_length=100)

    def __str__(self):
        return self.name


# Описание специальной подготовки перед проведением инструментального исследования.
# Например, натощак или за 30 минут до еды
class Preparation(models.Model):
    name = models.CharField(unique=True, max_length=40)

    # Наверное, лучше использовать TextField - в этом поле в админке отображается больше текста
    description = models.TextField(max_length=2000)

    def __str__(self):
        return self.name


# Карточка с описанием и стоимостью конкретного инструментального исследования.
# Например, УЗИ органов брюшной полости
class InstrumentalResearchCard(models.Model):
    i_r = models.OneToOneField(InstrumentalResearch, on_delete=models.CASCADE)
    description = models.TextField(max_length=2000)
    preparations = models.ManyToManyField(Preparation)
    price = models.PositiveIntegerField()

    # Почему-то interesting_fact = models.CharField(max_length=2000, default='') при заполнении через админку не давало
    # сохранить карточку с пустым полем "Интересный факт"
    # Наверное, лучше использовать TextField - в этом поле в админке отображается больше текста
    interesting_fact = models.TextField(max_length=2000, blank=True)

    def __str__(self):
        return self.i_r.name
