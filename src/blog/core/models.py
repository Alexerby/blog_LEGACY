from django.db import models

from django_ckeditor_5.fields import CKEditor5Field


class ContentSnippet(models.Model):
    title = models.CharField(max_length=100, null=True)
    ident = models.CharField(max_length=50, db_index=True)
    content = CKEditor5Field('content', config_name = 'extends')

    def __str__(self):
        return self.ident



