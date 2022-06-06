from django.db import models

# Create your models here.

class Fooditems(models.Model):
    foodid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length = 30)
    minutes = models.IntegerField()
    n_steps = models.IntegerField()
    steps = models.JSONField()
    ingredients = models.JSONField()
    n_ingredients = models.IntegerField()


