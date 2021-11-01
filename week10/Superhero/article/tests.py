from django.test import TestCase
from markdown import markdown

class DocTest(TestCase):
    def test_markdown(self):
        markdown_text = '# Headline'
        html_text = markdown(markdown_text)
        self.assertEqual(html_text, '<h1>Headline</h1>')

    def test_article_index_view(self):
        response = self.client.get('/article/')
        self.assertEqual(response.status_code, 200)

    def test_article_default_view(self):
        response = self.client.get('/article')
        self.assertEqual(response.status_code, 301)
        self.assertEqual(response.url, '/article/')
