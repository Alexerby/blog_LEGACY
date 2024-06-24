from django.urls import include, path
from blog.settings import base as settings 
from django.conf.urls.static import static

from .views import HomePageView

app_name = 'core'

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
