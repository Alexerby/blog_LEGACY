from django.db import models
from django.shortcuts import reverse
from django_ckeditor_5.fields import CKEditor5Field
from autoslug import AutoSlugField



class BoatListing(models.Model):

    title = models.CharField(max_length=80)
    description = CKEditor5Field('Description', null=True, blank=True)
    slug = AutoSlugField(populate_from='title', unique=True, default=None)
    price = models.PositiveIntegerField()
    thumbnail = models.ImageField(upload_to='boating/thumbnails')
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('boating:boat', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

class Engine(models.Model):
    boat_listing = models.OneToOneField('BoatListing', on_delete=models.CASCADE, related_name='engine')
    make = models.CharField(max_length=80)
    model = models.CharField(max_length=80)
    year = models.PositiveIntegerField(
            help_text = 'Enter the year of the engine manufacture.'
            )
    sterndrive = models.CharField(max_length=80)

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"

class Picture(models.Model):
    boat_listing = models.ForeignKey(BoatListing, related_name='pictures', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='boat_pictures/')
    description = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"Picture for {self.boat_listing.title}"

class Overview(models.Model):


    MOTORBOAT = 'motorboat'
    SAILBOAT = 'sailboat'

    BOAT_TYPE_CHOICES = [
        (MOTORBOAT, 'Motorboat'),
        (SAILBOAT, 'Sailboat'),
    ]

    boat_listing = models.OneToOneField('BoatListing', on_delete=models.CASCADE, related_name='overview')
    year = models.PositiveIntegerField()
    boat_type = models.CharField(max_length=20, choices=BOAT_TYPE_CHOICES, null=True)
    top_speed = models.PositiveIntegerField()

    def __str__(self):
        return f"{BoatListing.title}"

class Dimension(models.Model):
    boat_listing = models.OneToOneField('BoatListing', on_delete=models.CASCADE, related_name='dimensions')
    length = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    beam = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.boat_listing.title}: {self.length}, {self.beam}"

class Construction(models.Model):
    boat_listing = models.OneToOneField('BoatListing', on_delete=models.CASCADE, related_name='constructions')
    title = models.CharField(max_length=100)
    value = models.CharField(max_length=100)

    def __str__(self):
        return f"{BoatListing.title}"
