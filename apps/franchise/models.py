import uuid

from django.db import models
from django.urls import reverse

class Franchise(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False,
        verbose_name="ID"
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True)
    description = models.TextField(max_length=1000)
    release_date = models.IntegerField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('franchise', kwargs={'franchise_slug': self.slug})

    class Meta:
        app_label = 'franchise'