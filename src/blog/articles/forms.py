from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        widgets = {
            'published': forms.CheckboxInput(),
        }

        fields = ['title', 'thumbnail', 'entry', 'content', 'author',
                  'published', 'references', 'category']

