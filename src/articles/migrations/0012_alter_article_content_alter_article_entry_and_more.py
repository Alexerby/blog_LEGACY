# Generated by Django 5.0.6 on 2024-06-26 23:11

import django.core.validators
import django_ckeditor_5.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0011_article_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True, verbose_name='Body'),
        ),
        migrations.AlterField(
            model_name='article',
            name='entry',
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True, validators=[django.core.validators.MaxLengthValidator(500)], verbose_name='Entry'),
        ),
        migrations.AlterField(
            model_name='article',
            name='references',
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True, verbose_name='References'),
        ),
    ]
