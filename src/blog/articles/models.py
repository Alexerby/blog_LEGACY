from django.db import models

from django.core.validators import MaxLengthValidator
from django_ckeditor_5.fields import CKEditor5Field
from django.conf import settings
from autoslug import AutoSlugField
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=100)
    thumbnail = models.FileField(upload_to='articles/thumbnails')
    entry = models.TextField(validators=[MaxLengthValidator(350)])
    content = CKEditor5Field('Body', config_name='extends')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False) 
    slug = AutoSlugField(populate_from='title', unique=True, default=None)  
    references = models.TextField(default=None, null=True, blank=True)
    
    def get_absolute_url(self):
        return reverse('articles:article', kwargs={'slug': self.slug})  


    def __str__(self):
        return str(self.title)