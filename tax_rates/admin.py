from django.contrib import admin

from tax_rates.models import TaxUnitValue


class TaxUnitValueAdmin(admin.ModelAdmin):
    ordering = ('-year', )


admin.site.register(TaxUnitValue, TaxUnitValueAdmin)
