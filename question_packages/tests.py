from django.test import TestCase, SimpleTestCase
from .models import Questions

class SimpleTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    def test_sq_page_status_code(self):
        response = self.client.get('/sq/')
        self.assertEqual(response.status_code, 200)
    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
    
class PostModelTest(TestCase):
    def setUp(self):
        Questions.objects.create(text='just a test')
    def test_text_content(self):
        post=Questions.objects.get(id=1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name, 'just a test')