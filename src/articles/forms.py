from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article

        fields = ['title', 
                  'author', 
                  'language',
                  'category', 
                  'thumbnail', 
                  'published',  
                  'entry', 
                  'content',
                  'references', 
                  ]

