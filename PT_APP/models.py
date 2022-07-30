from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from autoslug import AutoSlugField


STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = AutoSlugField(populate_from='name', editable=True, always_update=True) # noqa
    featured_image = CloudinaryField('image', default='placeholder')
    location = models.CharField(max_length=200, blank=True)
    price = models.DecimalField(
        decimal_places=2,
        default=0,
        max_digits=11,)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.name

