# Generated by Django 5.0.6 on 2024-05-23 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0006_alter_workreference_job_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workreference',
            name='category',
            field=models.CharField(choices=[('experience', 'Experience'), ('education', 'Education'), ('technical', 'Technical Strengths'), ('other', 'Other')], max_length=20, null=True),
        ),
    ]
