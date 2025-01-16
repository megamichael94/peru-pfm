from django.contrib import admin

from .models import Payment, Enterprise, Income, Outcome, LineOfBusiness


@admin.register(Income, Outcome)
class IncomeOutcomeAdmin(admin.ModelAdmin):
    """"""

admin.site.register(Enterprise)
admin.site.register(LineOfBusiness)

