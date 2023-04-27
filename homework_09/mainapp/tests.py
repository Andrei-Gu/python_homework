from django.test import TestCase
from .models import InstrumentalResearchCategory, InstrumentalResearch


class TestInstrumentalResearchCategory(TestCase):

    def setUp(self) -> None:
        self.instr_res_category = InstrumentalResearchCategory.objects.create(short_name='mrt')


    def tearDown(self) -> None:
        print('А tearDown отрабатывает даже если тест упал?')


    def test_get_absolute_url(self):
        self.assertEqual(self.instr_res_category.get_absolute_url(), '/ir-category/1/')


    def test_get_short_name_url(self):
        self.assertEqual(self.instr_res_category.get_short_name_url(), '/ir-category/mrt/')


class TestInstrumentalResearch(TestCase):

    def setUp(self) -> None:
        instr_res_category = InstrumentalResearchCategory.objects.create(short_name='mrt')
        self.instrumental_research = InstrumentalResearch.objects.create(i_r_category=instr_res_category)


    def tearDown(self) -> None:
        print('Что происходит с другим принтом в tearDown? Почему в начале строки появляется точка?')


    def test_get_absolute_url(self):
        self.assertEqual(self.instrumental_research.get_absolute_url(), '/ir-category/mrt/1/')
