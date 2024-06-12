from django.shortcuts import render
from .models import Article
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from hitcount.views import HitCountDetailView


app_name = 'articles'


class ArticleListView(ListView):
    model = Article
    template_name = 'articles/article-list.html'  
    context_object_name = 'articles'  
    ordering = ['created_at']

    paginate_by = 10

    def get_queryset(self):
        return Article.objects.order_by('created_at')


class ArticleDetailView(HitCountDetailView):
    model = Article
    template_name = 'articles/article.html'
    context_object_name = 'article'
    count_hit = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = self.object
        context['article'] = article
        return context
