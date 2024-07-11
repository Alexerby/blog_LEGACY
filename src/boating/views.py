from django.shortcuts import Http404, render
from django.views.generic import TemplateView, DetailView, ListView
from .models import BoatListing, Engine, Picture, Overview, Dimension, Construction
from django.urls import reverse



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
    context_object_name = 'boats'
    ordering = ['created_at']
    template_name = 'boating/for-sale/index.html'

    def get_title(self):
        self.title = 'Till Salu'
        return self.title

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['title'] = self.get_title()
        return context

    def get_queryset(self):
        return BoatListing.objects.filter(published=True)

class BoatDetailView(DetailView):
    model = BoatListing
    template_name = 'boating/for-sale/boat.html'
    context_object_name = 'boat'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if not obj.published:
            raise Http404("Boat not found")
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['boat'].overview = self.object.overview
        
        if hasattr(self.object, 'overview'):
            excluded_fields = ['id', 'boat_listing']  # Fields to exclude
            
            overview_fields = []
            for field in self.object.overview._meta.get_fields():
                if field.name.startswith('_') or field.name in excluded_fields:
                    continue
                
                field_data = {
                    'name': field.verbose_name.capitalize(),
                    'value': getattr(self.object.overview, field.name, None),
                }
                overview_fields.append(field_data)
            
            context['overview_fields'] = overview_fields
        
        return context
