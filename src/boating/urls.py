
from django.urls import path
from .views import BoatingPageView, BoatsForSaleView



app_name = 'boating'

urlpatterns = [
    path('', BoatingPageView.as_view(), name='index'),
    path('boats-for-sale/', BoatsForSaleView.as_view(), name='boats-for-sale'),
]



