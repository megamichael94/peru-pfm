from django.db import models
from django.utils.timezone import now
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from PIL import Image


class LineOfBusiness(models.Model):
    """
    Line of business of enterprises
    """

    name = models.CharField(_('name'), max_length=512)
    code = models.IntegerField(_('code'), unique=True)

    class Meta:
        verbose_name = _('Line of business')
        verbose_name_plural = _('Line of businesses')

    def __str__(self):
        return self.name


class Enterprise(models.Model):
    """
    Enterprise model containing data related to the enterprise
    """

    name = models.CharField(_('name'), max_length=512)
    id_number = models.CharField(_('id number'), max_length=15, blank=True)
    line_of_business = models.ForeignKey(
        LineOfBusiness,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name=_('line of business'),
    )

    class Meta:
        verbose_name = _('Enterprise')
        verbose_name_plural = _('Enterprises')

    def __str__(self):
        return self.name


class Payment(models.Model):
    """
    Payment base model for incomes and outcomes
    #todo: add function delete remove file
    """

    file = models.FileField(_('file'), blank=True)
    image = models.ImageField(_('image'), blank=True)
    creation_datetime = models.DateTimeField(
        _('creation date '), auto_now_add=True)
    issue_date = models.DateField(_('date issued'), default=now)
    total = models.FloatField(_('total'), )
    taxes_percentage = models.IntegerField(_('taxes percentage'), default=10)
    taxes = models.FloatField(_('taxes amount'), null=True, blank=True)
    total_without_taxes = models.FloatField(
        _('total without taxes'), null=True, blank=True)
    is_it_tax_deductible = models.BooleanField(
        _('is tax deductible'), default=True)
    issuer = models.ForeignKey(
        Enterprise,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name=_('issuer')
    )

    class Meta:
        abstract = True

    def clean(self):
        # todo: test value of file and image when empty
        if self.file == '' and self.image == '':
            raise ValidationError(_('File and Image can not both be empty'))

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