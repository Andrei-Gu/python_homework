from django.test import TestCase
from .models import InstrumentalResearchCategory, InstrumentalResearch


class TestViews(TestCase):

    def test_status_code(self):
        paths = ('/',
                 '/success-result/',
                 '/ir-category-list/',
                 '/ir-category-create/',
                 '/instr-research-create/',
                 )
        for path in paths:
            response = self.client.get(path)
            # использование параметра msg упрощает процесс
            self.assertEqual(response.status_code, 200, msg=f'Проверку на доступность не прошел URL: {path}')


    def test_ir_categories_context_processor(self):
        response = self.client.get('/')
        self.assertTrue('all_ir_categories' in response.context)


    def test_ir_categories_list(self):
        InstrumentalResearchCategory.objects.create(name='Рентген')
        response = self.client.get('/ir-category-list/')
        self.assertTrue('instrumentalresearchcategory_list' in response.context)
        self.assertEqual(response.context['instrumentalresearchcategory_list'].first().name, 'Рентген')


    def test_specific_ir_category_list(self):
        instr_res_category = InstrumentalResearchCategory.objects.create(short_name='uzi')
        instrumental_research = InstrumentalResearch.objects.create(i_r_category=instr_res_category)
        response = self.client.get('/ir-category/uzi/')
        self.assertTrue('instrumentalresearch_list' in response.context)
        self.assertEqual(response.context['instrumentalresearch_list'].first().id, instrumental_research.id)


    def test_btn_create_on_ir_category_list_content(self):
        response = self.client.get('/ir-category-list/')
        button_create = '<a class="btn btn-primary" href="/ir-category-create/">Создать категорию</a>'
        # Декодируем содержимое контента из байтов и проверяем вхождение
        self.assertIn(button_create, response.content.decode(encoding='utf-8'))

        # Кодируем код кнопки в байты и проверяем вхождение в контент
        self.assertIn(button_create.encode(encoding='utf-8'), response.content)
