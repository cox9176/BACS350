from django.views.generic import RedirectView, TemplateView
from markdown import markdown

class DocumentView(TemplateView):
    template_name = 'article.html'

    def get_context_data(self, **kwargs):
        document = self.kwargs.get('article', 'index')
        markdown_text = open(f'documents/{document}.md').read()
        return dict(article=markdown(markdown_text), file=document)

