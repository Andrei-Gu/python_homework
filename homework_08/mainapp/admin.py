from django.contrib import admin
from .models import InstrumentalResearchCategory, InstrumentalResearch, Preparation, InstrumentalResearchCard


admin.site.register(InstrumentalResearchCategory)
admin.site.register(InstrumentalResearch)
admin.site.register(Preparation)
admin.site.register(InstrumentalResearchCard)