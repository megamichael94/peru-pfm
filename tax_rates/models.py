from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class UITValue(models.Model):
    year = models.IntegerField(
        default=2022, validators=[
            MaxValueValidator(2100), MinValueValidator(1994)], unique=True)
    value = models.FloatField()


class Chunk(models.Model):
    min_value_range = models.FloatField()
    max_value_range = models.FloatField()