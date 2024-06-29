# Generated by Django 5.0.6 on 2024-06-25 19:55

import django.core.validators
import django_ckeditor_5.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_alter_article_entry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='entry',
            field=django_ckeditor_5.fields.CKEditor5Field(validators=[django.core.validators.MaxLengthValidator(500)], verbose_name='Entry'),
        ),
    ]