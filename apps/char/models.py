import uuid
from django.db import models
from django.urls import reverse

class Character(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False,
        verbose_name="ID"
    )
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    description = models.TextField(max_length=1000)
    franchise = models.ForeignKey('franchise.Franchise', related_name='characters', on_delete= models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True)
    role = models.CharField(max_length=100, null=True)
    age = models.IntegerField(null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('char', kwargs={'char_slug': self.slug})

    class Meta:
        app_label = 'char'
