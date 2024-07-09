from django.db import models
from django.shortcuts import reverse
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
    price = models.PositiveIntegerField()
    thumbnail = models.ImageField(upload_to='boating/thumbnails')
    year = models.PositiveIntegerField()
    description = CKEditor5Field('Description', null=True, blank=True)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(populate_from='title', unique=True, default=None)
    boat_type = models.CharField(max_length=20, choices=BOAT_TYPE_CHOICES, null=True)
    engine = models.ForeignKey('Engine', on_delete=models.CASCADE, null=True, blank=True)
    top_speed = models.PositiveIntegerField()
    length = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    beam = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('boating:boat', kwargs={'slug': self.slug})

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

class Picture(models.Model):
    boat_listing = models.ForeignKey(BoatListing, related_name='pictures', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='boat_pictures/')
    description = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"Picture for {self.boat_listing.title}"
