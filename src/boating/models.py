from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from autoslug import AutoSlugField

class BoatListing(models.Model):
    MOTORBOAT = 'motorboat'
    SAILBOAT = 'sailboat'
    BOAT_TYPE_CHOICES = [
        (MOTORBOAT, 'Motorboat'),
        (SAILBOAT, 'Sailboat'),
    ]

    title = models.CharField(max_length=80)
    description = CKEditor5Field('Description', null=True, blank=True)
    published = models.BooleanField(default=False)
    slug = AutoSlugField(populate_from='title', unique=True, default=None)
    boat_type = models.CharField(max_length=20, choices=BOAT_TYPE_CHOICES, null=True)
    engine = models.ForeignKey('Engine', on_delete=models.CASCADE, null=True, blank=True)
    length = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    beam = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.title

class Engine(models.Model):
    make = models.CharField(max_length=80)
    model = models.CharField(max_length=80)
    year = models.PositiveIntegerField(
            help_text = 'Enter the year of the engine manufacture.'
            )

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"

