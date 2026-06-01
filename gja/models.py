from django.db import models

# Create your models here.
class Member(models.Model):

    CATEGORY_CHOICES = [
        ('gem', 'Gem'),
        ('jewellery', 'Jewellery'),
        ('watch', 'Watch'),
        ('design', 'Design'),
    ]

    name = models.CharField(max_length=200)
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES
    )

    description = models.TextField()
    logo = models.ImageField(upload_to='members/')

    def __str__(self):
        return self.name


class Event(models.Model):

    title = models.CharField(max_length=255)

    slug = models.SlugField(unique=True)

    short_description = models.TextField()

    description = models.TextField()

    image = models.ImageField(
        upload_to='events/'
    )

    start_date = models.DateField()

    end_date = models.DateField()

    location = models.CharField(
        max_length=255
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return self.title