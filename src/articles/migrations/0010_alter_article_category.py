# Generated by Django 5.0.6 on 2024-06-25 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_alter_article_entry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(choices=[('boating', 'Boating'), ('motorcycling', 'Motorcycling'), ('software_development', 'Software Development'), ('investing', 'Investing'), ('other', 'Other'), ('politics', 'Politics')], max_length=20, null=True),
        ),
    ]
