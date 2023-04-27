from .models import InstrumentalResearchCategory

def rendering_categories(request):
    return {'all_ir_categories': InstrumentalResearchCategory.objects.all()}