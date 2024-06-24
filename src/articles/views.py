from django.shortcuts import render

from user.mixins import GroupMixin
from .models import Article
from django.views.generic.detail import DetailView
from django.views.generic import DeleteView, ListView, CreateView, UpdateView
from hitcount.views import HitCountDetailView
from django.urls import reverse, reverse_lazy
from django.contrib.admin.views.decorators import staff_member_required

from .forms import ArticleForm

from user.mixins import StaffRequiredMixin


app_name = 'articles'


class ArticleListView(ListView):
    model = Article
    template_name = 'articles/article-list.html'  
    context_object_name = 'articles'  
    ordering = ['created_at']

    paginate_by = 10

    def get_queryset(self):
        return Article.objects.order_by('created_at')


class ArticleDetailView(GroupMixin, HitCountDetailView):
    model = Article
    template_name = 'articles/article.html'
    context_object_name = 'article'
    count_hit = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = self.object
        context['article'] = article
        context['user_is_editor'] = self.user_in_group('Editor')
        return context

class AddPostView(StaffRequiredMixin, CreateView):

    model = Article
    template_name = 'articles/add_post.html'
    form_class = ArticleForm

    def get_absolute_url(self):
        return reverse('article', args=(str(self.id)))


class UpdatePostView(StaffRequiredMixin, UpdateView):

    model = Article
    template_name = 'articles/update_post.html'
    form_class = ArticleForm

    def get_absolute_url(self):
        return reverse('article', args=(str(self.id)))


class DeletePostView(StaffRequiredMixin, DeleteView):

    model = Article
    template_name = 'articles/delete_post.html'
    success_url = reverse_lazy('articles:index')

