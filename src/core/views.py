from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from articles.models import Article
from .models import ContentSnippet

class HomePageView(ListView):
    template_name = 'core/home.html'
    context_object_name = 'articles'
    queryset = Article.objects.order_by('created_at')

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Retrieve ContentSnippet entries
        content_snippets = ContentSnippet.objects.filter(ident__in=["introduction", "about"])
        snippets = {snippet.ident: snippet for snippet in content_snippets}
        
        context['content_snippet_intro'] = snippets.get("introduction")
        context['about'] = snippets.get("about")
        
        return context
