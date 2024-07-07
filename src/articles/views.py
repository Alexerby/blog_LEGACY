from django.shortcuts import render

from user.mixins import GroupMixin
from .models import Article
from django.views.generic.detail import DetailView
from django.views.generic import DeleteView, ListView, CreateView, UpdateView
from hitcount.views import HitCountDetailView
from django.urls import reverse, reverse_lazy
from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404

from .forms import ArticleForm

from user.mixins import StaffRequiredMixin


app_name = 'articles'


class ArticleListView(GroupMixin, ListView):
    model = Article
    template_name = 'articles/article-list.html'  
    context_object_name = 'articles'  
    ordering = ['created_at']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_is_editor'] = self.user_in_group('Editor')
        return context

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

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        article = self.object

        # Check if the article is not published and the user is not an editor
        if not article.published and not self.user_in_group('Editor'):
            raise Http404("Article not found")

        return super().get(request, *args, **kwargs)



class ManageArticlesListView(ArticleListView):
    template_name = 'articles/manage/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_is_editor'] = self.user_in_group('Editor')
        return context


class AddPostView(StaffRequiredMixin, CreateView):
    model = Article
    template_name = 'articles/manage/add_post.html'
    form_class = ArticleForm

    def get_success_url(self):
        return reverse('articles:article', args=[self.object.slug])


class UpdatePostView(StaffRequiredMixin, UpdateView):
    model = Article
    template_name = 'articles/manage/update_post.html'
    form_class = ArticleForm

    def get_success_url(self):
        return reverse('articles:article', args=[self.object.slug])


class DeletePostView(StaffRequiredMixin, DeleteView):

    model = Article
    template_name = 'articles/manage/delete_post.html'
    success_url = reverse_lazy('articles:index')

