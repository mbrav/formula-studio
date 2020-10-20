from django.db import models

# Create your models here.

class Book(models.Model):
    STATUS = (
        (0,'Unknown'),
        (1,'Processed'),
        (2,'Paid')
    )

    title = models.CharField(max_length=36, blank=False, unique=True, default='')

    description = models.TextField(max_length=256, blank=True)

    price = models.DecimalField(default=0, decimal_places=2, max_digits=10, blank=True)
    is_available= models.BooleanField(default=False)

    published = models.DateField(auto_now=True, blank=True, null=True)
    is_published = models.BooleanField(default=False)

    # cover = models.FileField(upload_to='covers/')
    cover = models.ImageField(upload_to='covers/', blank=True)
