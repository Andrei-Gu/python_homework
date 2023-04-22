from django.db import models


# Вид инструментального исследования, напримре, МРТ, КТ, рентген, УЗИ
class InstrumentalResearchCategory(models.Model):
    name = models.TextField(unique=True, max_length=40)
    short_name = models.CharField(unique=True, max_length=10)
    description = models.TextField(max_length=2000)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

# Конкретное инструментальное исследование, например, рентген стопы или УЗИ сосудов
class InstrumentalResearch(models.Model):
    i_r_category = models.ForeignKey(InstrumentalResearchCategory, on_delete=models.CASCADE)
    name = models.TextField(unique=True, max_length=100)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

# Описание специальной подготовки перед проведением инструментального исследования.
# Например, натощак или за 30 минут до еды
class Preparation(models.Model):
    name = models.TextField(max_length=40)
    description = models.TextField(max_length=2000)

    def __str__(self):
        return self.name

# Карточка с описанием и стоимостью конкретного инструментального исследования.
# Например, УЗИ органов брюшной полости
class InstrumentalResearchCard(models.Model):
    instrumental_research = models.OneToOneField(InstrumentalResearch, on_delete=models.CASCADE)
    i_r_description = models.TextField(max_length=2000)
    i_r_preparation = models.ManyToManyField(Preparation)
    i_r_price = models.PositiveIntegerField()
    i_r_interesting_fact = models.TextField(max_length=2000, blank=True)

    def __str__(self):
        return self.instrumental_research.name
