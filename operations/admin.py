from django.contrib import admin

from .models import LineOfBusiness, Enterprise, Income, Outcome


@admin.register(Income, Outcome)
class IncomeOutcomeAdmin(admin.ModelAdmin):
    """Admin class for incomes and outcomes"""


admin.site.register(Enterprise)
admin.site.register(LineOfBusiness)
