from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
from .models import BoatListing



class BoatingPageView(TemplateView):
    template_name = 'boating/index.html'

    def get_title(self):
        self.title = 'Båtverksamhet'
        return self.title

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_title()

        return context

class BoatsForSaleView(ListView):
    model = BoatListing

    template_name = 'boating/for-sale/index.html'

    def get_title(self):
        self.title = 'Till Salu'
        return self.title

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        return context

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(published=True)

