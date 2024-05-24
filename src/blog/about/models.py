from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class AboutSection(models.Model):
    title = models.CharField(max_length=100)
    content = CKEditor5Field('content', config_name = 'extends')

    def __str__(self):
        return self.title

class WorkReference(models.Model):
    CATEGORY_CHOICES = [
        ('experience', 'Experience'),
        ('education', 'Education'),
        ('technical', 'Technical Strengths'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=100)
    description = CKEditor5Field('content', config_name='extends')
    file = models.FileField(upload_to='references/', blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, null=True)
    job_title = models.CharField(max_length=70, blank=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title
