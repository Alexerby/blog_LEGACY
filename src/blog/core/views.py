from django.shortcuts import render
from django.views.generic import TemplateView

from articles.models import Article
from .models import ContentSnippet

class HomePageView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Retrieve articles
        articles = Article.objects.order_by('created_at')
        context['articles'] = articles
        
        # Retrieve ContentSnippet entries
        content_snippets = ContentSnippet.objects.filter(ident__in=["introduction", "about"])
        snippets = {snippet.ident: snippet for snippet in content_snippets}
        
        context['content_snippet_intro'] = snippets.get("introduction")
        context['about'] = snippets.get("about")
        
        return context
