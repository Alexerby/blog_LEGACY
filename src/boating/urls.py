from django.urls import path
from .views import BoatingPageView, BoatsForSaleView, BoatDetailView

app_name = 'boating'

urlpatterns = [
    path('', BoatingPageView.as_view(), name='index'),
    path('boats-for-sale/', BoatsForSaleView.as_view(), name='boats-for-sale'),
    path('boats-for-sale/<slug:slug>/', BoatDetailView.as_view(), name='boat'),
]
