from django.urls import include, path

from .views import HomePageView

app_name = 'core'

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
] 
