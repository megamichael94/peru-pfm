from django.db import models
from django.utils.timezone import now
from django.core.exceptions import ValidationError

from PIL import Image


#ToDo: add translatable verbose name

class LineOfBusiness(models.Model):
    """
    Rubro del negocio
    """

    name = models.CharField(max_length=512)
    code = models.IntegerField(unique=True)

    def __str__(self):
        return self.name


class Enterprise(models.Model):
    """
    Empresa
    """

    name = models.CharField(max_length=512)
    id_number = models.CharField(max_length=15, blank=True)
    line_of_business = models.ManyToManyField(
        LineOfBusiness, blank=True, related_name='enterprises'
    )

    def __str__(self):
        return self.name


class Payment(models.Model):
    """
    Pago
    #todo: add function delete remove file
    """

    file = models.FileField(blank=True)
    image = models.ImageField(blank=True)
    creation_datetime = models.DateTimeField(auto_now_add=True)
    issue_date = models.DateField(default=now)
    total = models.FloatField()
    taxes_percentage = models.IntegerField(default=10)
    taxes = models.FloatField(null=True, blank=True)
    total_without_taxes = models.FloatField(null=True, blank=True)
    is_it_tax_deductible = models.BooleanField(default=True)
    issuer = models.ForeignKey(
        Enterprise, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        abstract = True

    def clean(self):
        # todo: test value of file and image when empty
        if self.file == '' and self.image == '':
            raise ValidationError('File and Image can not both be empty')

    def __str__(self):
        enterprise = self.issuer or '-'
        date = self.issue_date.strftime('%Y-%m-%d')
        return f"{enterprise} {self.total} {date}"

    def save(self, *args, **kwargs):
        if self.taxes_percentage:
            self.taxes = round(
                self.total / (1 + self.taxes_percentage / 100), 2)
            self.total_without_taxes = self.total - self.taxes

        instance = super().save(args, kwargs)
        return instance


class Income(Payment):
    ...


class Outcome(Payment):
    ...