from django.db import models

# Create your models here.
class Image(models.Model):
    imgid = models.IntegerField(primary_key=True)
    img = models.ImageField(upload_to="photos/",null=True, blank=True)

