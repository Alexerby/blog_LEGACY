# Generated by Django 5.0.6 on 2024-07-11 14:42

import django.db.models.deletion
import django_ckeditor_5.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boating', '0011_remove_construction_slug_boatlisting_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='overview',
            name='description',
        ),
        migrations.AddField(
            model_name='boatlisting',
            name='description',
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='overview',
            name='boat_listing',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='overview', to='boating.boatlisting'),
        ),
    ]
