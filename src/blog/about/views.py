from django.views.generic import TemplateView
from django.core.files.storage import default_storage

from .models import AboutSection, WorkReference
from core.models import ContentSnippet


class AboutPageView(TemplateView):
    template_name = 'about/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about_sections'] = AboutSection.objects.all()
        
        work_references = WorkReference.objects.all()
        categories = WorkReference.CATEGORY_CHOICES
        grouped_references = {category[0]: [] for category in categories}

        for reference in work_references:
            grouped_references[reference.category].append(reference)

        context['grouped_references'] = grouped_references
        context['categories'] = categories

        content_snippets = ContentSnippet.objects.filter(ident__in=["introduction", "about"])
        snippets = {snippet.ident: snippet for snippet in content_snippets}
        context['about'] = snippets.get("about")


        return context
