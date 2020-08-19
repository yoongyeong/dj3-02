from django.db import models


class Cluster(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    cluster = models.ForeignKey(Cluster, on_delete=models.DO_NOTHING)
    description = models.TextField(max_length=200)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    area_width = models.IntegerField(default=None)
    area_length = models.IntegerField(default=None)
    features = models.TextField()
    is_promo = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)
    is_on_slide = models.BooleanField(default=False)
    image_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    image_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    image_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    image_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    image_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    image_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    image_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.name
