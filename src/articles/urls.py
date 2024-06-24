from django.urls import path

from .views import ArticleDetailView, ArticleListView, AddPostView, DeletePostView, UpdatePostView



app_name = 'articles'

urlpatterns = [
    path('', ArticleListView.as_view(), name='index'),
    path('manage/add/', AddPostView.as_view(), name='add'),
    path('manage/edit/<slug:slug>', UpdatePostView.as_view(), name='edit'),
    path('manage/delete/<slug:slug>', DeletePostView.as_view(), name='delete'),
    path('<slug:slug>/', ArticleDetailView.as_view(), name='article'),
]



