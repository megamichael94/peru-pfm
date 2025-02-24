from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class TaxUnitValue(models.Model):
    """
    This value is known in Peru as UIT
    """

    year = models.IntegerField(
        default=2022, validators=[
            MaxValueValidator(2100), MinValueValidator(1994)], unique=True)
    value = models.FloatField()

    def __str__(self):
        return f'{self.year} {self.value}'


class Chunk(models.Model):
    """This model will be used to get a tax range"""
    min_value_range = models.FloatField()
    max_value_range = models.FloatField()
