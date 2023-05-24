from django.contrib import admin

from .models import Payment, Enterprise, Income, Outcome

#
# class DetailInLine(admin.TabularInline):
#     model = Detail
#
#
@admin.register(Income, Outcome)
class IncomeAdmin(admin.ModelAdmin):
    """"""


admin.site.register(Enterprise)

